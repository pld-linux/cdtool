Summary:	Powerful command line CDROM player and tools.
Summary(pl):	Odtwarzacz p造t CD wywo造wany z linii komend
Name:		cdtool
Version:	2.1.5
Release:	1
Copyright:	GPL
Group:		Utilities/System
Group(pl):	Narz璠zia/System
Source:		ftp://sunsite.unc.edu/pub/Linux/apps/sound/cdrom/cli/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
A package of command-line utilities to play and catalog audio CD-ROMs.  This
package includes cdstart, cdpause, cdstop, cdeject, and cdshuffle. Also,
cdctrl may be used as a CD-ROM control daemon. Cdown allows querying of the
cddb database to build a local database of discs usable by cdinfo, etc.

%description -l pl
Pakiet zawiera odtwarzacz p造t CD wywo造wany z lini komend. Korzysta z CDDB.

%prep
%setup -q

%build
make clean noobjs cdown cdadd DEBUG_FLAGS="$RPM_OPT_FLAGS"
make cdctrl DEBUG_FLAGS="$RPM_OPT_FLAGS -s -DCDCTRL"
make noobjs
make cdtool links DEBUG_FLAGS="$RPM_OPT_FLAGS -s"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install cd{ctrl,ir,eject,info,loop,add,own,pause,reset,shuffle,start,stop,tool} \
	$RPM_BUILD_ROOT%{_bindir}
install {cdtool,cdctrl,cdown}.1 $RPM_BUILD_ROOT%{_mandir}/man1

echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdstart.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdpause.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdstop.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdeject.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdir.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdinfo.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdreset.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdshuffle.1

gzip -9nf {README,cdtool-2.1.5.lsm,$RPM_BUILD_ROOT%{_mandir}/man1/*}

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%doc {README,cdtool-2.1.5.lsm}.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
