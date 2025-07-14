Summary:	Powerful command line CDROM player and tools
Summary(pl.UTF-8):	Odtwarzacz płyt CD wywołany z linii poleceń
Name:		cdtool
Version:	2.1.8
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://hinterhof.net/cdtool/dist/%{name}-%{version}.tar.gz
# Source0-md5:	7b19b6f68d2c648296378b784d5f7681
Patch0:		%{name}-install.patch
URL:		http://hinterhof.net/cdtool/
# /usr/bin/cdplay with similar functionality - what to do?
Conflicts:	cdp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A package of command-line utilities to play and catalog audio CD-ROMs.
This package includes cdstart, cdpause, cdstop, cdeject, and
cdshuffle. Also, cdctrl may be used as a CD-ROM control daemon. cdown
allows querying of the cddb database to build a local database of
discs usable by cdinfo, etc.

%description -l pl.UTF-8
Pakiet działających z linii poleceń narzędzi do odtwarzania i
katalogowania płyt CD Audio. Zawiera cdstart, cdpause, cdstop, cdeject
i cdshuffle. Program cdctrl może być używany także jako demon do
sterowania płytami CD. cdown umożliwia odpytywanie bazy cddb w celu
zbudowania lokalnej bazy danych płyt używalnej dla cdinfo itp.

%prep
%setup -q
%patch -P0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CREDITS README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/cdtool
%attr(755,root,root) %{_libdir}/cdtool/cdtool
%{_mandir}/man1/*
