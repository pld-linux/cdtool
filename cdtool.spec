Summary:	Powerful command line CDROM player and tools
Summary(pl):	Odtwarzacz p³yt CD wywo³any z linii poleceñ
Name:		cdtool
Version:	2.1.8pre1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://hinterhof.net/cdtool/dist/%{name}-%{version}.tar.gz
# Source0-md5:	6f6e3740d5c5525b3c0067b043310a3c
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

%description -l pl
Pakiet dzia³aj±cych z linii poleceñ narzêdzi do odtwarzania i
katalogowania p³yt CD Audio. Zawiera cdstart, cdpause, cdstop, cdeject
i cdshuffle. Program cdctrl mo¿e byæ u¿ywany tak¿e jako demon do
sterowania p³ytami CD. cdown umo¿liwia odpytywanie bazy cddb w celu
zbudowania lokalnej bazy danych p³yt u¿ywalnej dla cdinfo itp.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# separate script, but documented in cdtool(1)
echo '.so cdadd.1' >$RPM_BUILD_ROOT%{_mandir}/man1/cdtool.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES PEOPLE README TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/cdtool
%attr(755,root,root) %{_libdir}/cdtool/cdtool
%{_mandir}/man1/*
