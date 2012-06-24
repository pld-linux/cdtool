Summary:	Powerful command line CDROM player and tools.
Summary(pl):	Odtwarzacz p�yt CD wywo�any z lini komend
Name:		cdtool
Version:	2.1.5
Release:	1
Copyright:	GPL
Group:		Utilities/System
Source:		sunsite.unc.edu:/pub/Linux/apps/sound/cdrom/cli/%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
A package of command-line utilities to play and
catalog audio CD-ROMs.  This package includes 
cdstart, cdpause, cdstop, cdeject, and cdshuffle.
Also, cdctrl may be used as a CD-ROM control daemon.
Cdown allows querying of the cddb database to build a 
local database of discs usable by cdinfo, etc.

%description(pl)
Pakiet zawiera odtwarzacz p�yt CD wywo�ywany z lini
komend. Korzysta z CDDB

%prep
%setup -q
%build
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install cdctrl $RPM_BUILD_ROOT%{_bindir}
install cdloop $RPM_BUILD_ROOT%{_bindir}
install cdadd  $RPM_BUILD_ROOT%{_bindir}
install cdown  $RPM_BUILD_ROOT%{_bindir}
install cdtool $RPM_BUILD_ROOT%{_bindir}
install cdtool.1 $RPM_BUILD_ROOT%{_mandir}/man1
install cdctrl.1 $RPM_BUILD_ROOT%{_mandir}/man1
install cdown.1 $RPM_BUILD_ROOT%{_mandir}/man1

echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdstart.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdpause.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdstop.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdeject.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdir.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdinfo.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdreset.1
echo .so cdtool.1 >$RPM_BUILD_ROOT%{_mandir}/man1/cdshuffle.1

ln -sf cdtool $RPM_BUILD_ROOT%{_bindir}/cdstart
ln -sf cdtool $RPM_BUILD_ROOT%{_bindir}/cdpause
ln -sf cdtool $RPM_BUILD_ROOT%{_bindir}/cdstop
ln -sf cdtool $RPM_BUILD_ROOT%{_bindir}/cdeject
ln -sf cdtool $RPM_BUILD_ROOT%{_bindir}/cdir
ln -sf cdtool $RPM_BUILD_ROOT%{_bindir}/cdinfo
ln -sf cdtool $RPM_BUILD_ROOT%{_bindir}/cdreset
ln -sf cdtool $RPM_BUILD_ROOT%{_bindir}/cdshuffle

gzip -9nf {README,COPYING,INSTALL,cdtool-2.1.5.lsm,$RPM_BUILD_ROOT%{_mandir}/man1/*}

%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man1/*
%doc {README,COPYING,INSTALL,cdtool-2.1.5.lsm}.gz
