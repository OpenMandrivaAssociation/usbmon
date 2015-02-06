%define name	usbmon
%define version	5.4
%define release	2

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



%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 5.4-1mdv2011.0
+ Revision: 645476
- update to new version 5.4

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 5.3-2mdv2010.0
+ Revision: 445614
- rebuild

* Tue Dec 23 2008 Pascal Terjan <pterjan@mandriva.org> 5.3-1mdv2009.1
+ Revision: 317783
- import usbmon


* Tue Dec 23 2008 Pascal Terjan <pterjan@mandriva.org> 5.3-1mdv2009.1
- Import into Mandriva

* Thu Dec 18 2008 Pete Zaitcev <zaitcev@redhat.com> 5.3-1
- Pull 5.3 in: license made explicit in usbmon.c per Fedora review feedback.
  Also, change parse_params to protect print_48 from overflows.

* Sun Dec 7 2008 Pete Zaitcev <zaitcev@redhat.com> 5.2-1
- Initial revision (5.2)
