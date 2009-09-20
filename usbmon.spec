%define name	usbmon
%define version	5.3
%define release	%mkrel 2

Name:		%name
Version:	%version
Release:	%release
Summary:	A basic front-end to usbmon
Group:		Development/Other
License:	GPLv2
URL:		http://people.redhat.com/zaitcev/linux/
Source:		http://people.redhat.com/zaitcev/linux/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The usbmon program collects and prints a trace of USB transactions as they
occur between the USB core and HCDs. Analyzing the trace helps to debug the
kernel USB stack, device firmware, and applications.

%prep
%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 -t $RPM_BUILD_ROOT/%{_mandir}/man8 usbmon.8
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
install -p -m 755 -t $RPM_BUILD_ROOT/%{_sbindir} usbmon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_sbindir}/usbmon
%{_mandir}/man8/usbmon.8*

