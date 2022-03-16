Name:		helloraidix
Version:	1.0
Release:	0
Summary:	A sample package, saing hello to RAIDIX
Group:		Applications/Productivity
License:	GPL
Source0:	helloraidix.tar.gz
BuildRequires:	gcc, make
Requires:    libc.so.6


%description
helloraidix is a simple utility that prints "Test task in RAIDIDX!"


%prep
%global debug_package %{nil}
%setup -q -n %{name}


%build
make


%install
make DESTDIR=$RPM_BUILD_ROOT/usr/local/bin install


%files
%defattr(-,root,root)
/usr/local/bin/helloraidix


%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Wed Mar 16 2022 Egor Bronnikov
- Initial build
