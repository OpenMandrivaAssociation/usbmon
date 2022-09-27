%undefine _debugsource_packages

Name:		usbmon
Version:	6.1
Release:	1
Summary:	A basic front-end to usbmon
Group:		Development/Other
License:	GPLv2
URL:		http://people.redhat.com/zaitcev/linux/
Source:		http://people.redhat.com/zaitcev/linux/%{name}-%{version}.tar.gz

%description
The usbmon program collects and prints a trace of USB transactions as they
occur between the USB core and HCDs. Analyzing the trace helps to debug the
kernel USB stack, device firmware, and applications.

%prep
%autosetup -p1

%build
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -p -m 644 -t $RPM_BUILD_ROOT/%{_mandir}/man8 usbmon.8
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 -t $RPM_BUILD_ROOT/%{_bindir} usbmon

%files
%defattr(-,root,root,-)
%doc README COPYING
%{_bindir}/usbmon
%{_mandir}/man8/usbmon.8*
