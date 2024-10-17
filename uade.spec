%define name uade
%define version 2.13
%define fname %name-%{version}
%define release 7

Summary: Unix Amiga Delitracker Emulator
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://zakalwe.fi/uade/uade2/%{fname}.tar.bz2
Patch: uade-2.13-new-audacious.patch
URL: https://zakalwe.fi/uade/
License: GPL
Group: Sound
BuildRequires: fuse-devel
BuildRequires: libao-devel
#gw for mod2ogg
Suggests: vorbis-tools
Suggests: normalize
Suggests: flac
Suggests: lame

%description
Plays old amiga tunes with UAE emulation and cloned m68k-assembler
Amiga delitracker API. With cloned delitracker API you don't have to
port old players from Amiga, you can re-use old Deliplayers that use
Amiga Delitracker API. Deliplayers are used like on Amiga, they exist
in some directory and you can copy/remove them as you wish. "Installing"
new players is just copying files to your 'players' directory.

%if 0
%package -n audacious-uade
Group: Sound
Summary: Unix Amiga Delitracker Emulator Audacious Media Player input plugin
BuildRequires: audacious-devel
Requires: audacious
Provides: beep-media-player-uade
Obsoletes: beep-media-player-uade
Requires: uade = %version

%description -n audacious-uade
Plays old amiga tunes with UAE emulation and cloned m68k-assembler
Amiga delitracker API. With cloned delitracker API you don't have to
port old players from Amiga, you can re-use old Deliplayers that use
Amiga Delitracker API. Deliplayers are used like on Amiga, they exist
in some directory and you can copy/remove them as you wish. "Installing"
new players is just copying files to your 'players' directory.

This is the input plugin for Audacious Media Player based on uade.
%endif

%prep
%setup -q -n %fname
%patch -p1
find songs -name CVS|xargs rm -rfv
chmod 644 songs/* AUTHORS ChangeLog
chmod 755 songs/
%build
export CFLAGS="%optflags"
./configure --prefix=%{_prefix} --libdir=%_libdir --package-prefix=%buildroot
%make

%install
rm -rf %buildroot
make install PACKAGEPREFIX=%buildroot BINDIR=%buildroot%_bindir DATADIR=%buildroot%_datadir/uade2 AUDACIOUSPLUGINDIR=%buildroot%_libdir/audacious/Input/
mv %buildroot%_bindir/mod2ogg2.sh %buildroot%_bindir/mod2ogg
%if %_lib != lib
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %buildroot%_prefix/lib/pkgconfig/* %{buildroot}%{_libdir}/pkgconfig
rm -rf %buildroot%_prefix/lib/pkgconfig/
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%doc songs
%{_bindir}/uade123
%{_bindir}/uadefs
%_bindir/mod2ogg
%{_datadir}/uade2
%_prefix/lib/uade2/
%{_libdir}/pkgconfig/uade.pc
%_mandir/man1/uade123.1*
%_mandir/man1/uadefs.1*

%if 0
%files -n audacious-uade
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/audacious/Input/libuade2.so
%endif


%changelog
* Sat Mar 31 2012 GÃ¶tz Waschk <waschk@mandriva.org> 2.13-5mdv2012.0
+ Revision: 788422
- yearly rebuild

* Wed Mar 30 2011 GÃ¶tz Waschk <waschk@mandriva.org> 2.13-4
+ Revision: 649063
- disable audacious plugin

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Sun Mar 28 2010 Funda Wang <fwang@mandriva.org> 2.13-3mdv2010.1
+ Revision: 528373
- rebuild

* Wed Feb 03 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.13-2mdv2010.1
+ Revision: 499941
- patch for new audacious

* Fri Nov 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.13-1mdv2010.1
+ Revision: 460844
- update to new version 2.13

* Wed May 13 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.12-2mdv2010.0
+ Revision: 375247
- rebuild for new audacious

* Thu Aug 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.12-1mdv2009.0
+ Revision: 276790
- new version

* Sun Jul 06 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.11-1mdv2009.0
+ Revision: 232284
- new version

* Mon Jun 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.10-2mdv2009.0
+ Revision: 227962
- rebuild for broken rpm

* Sun Jun 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.10-1mdv2009.0
+ Revision: 227944
- fix buildrequires
- new version
- add uadefs

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sun Dec 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.09-1mdv2008.1
+ Revision: 139671
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 18 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.08-1mdv2008.1
+ Revision: 109938
- fix installation
- new version
- drop patch
- update file list
- fix URL

* Wed Oct 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.07-2mdv2008.1
+ Revision: 99565
- readd suggests
- patch to make the audacious plugin suppor audacious 1.4

* Wed Jul 04 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.07-1mdv2008.1
+ Revision: 48111
- remove dep on lha

* Wed May 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.07-1mdv2008.0
+ Revision: 20408
- new version

* Tue Apr 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.06-1mdv2007.1
+ Revision: 13640
- new version


* Fri Jan 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.05-1mdv2007.0
+ Revision: 113612
- new version

* Sun Jan 21 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.04-1mdv2007.1
+ Revision: 111452
- fix installation on x86_64
- Import uade

* Sun Jan 21 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.04-1mdv2007.1
- New version 2.04

* Mon Aug 28 2006 Götz Waschk <waschk@mandriva.org> 2.03-1mdv2007.0
- update file list
- New release 2.03

* Tue May 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.02-3mdk
- rebuild for new audacious

* Sat May 06 2006 Götz Waschk <waschk@mandriva.org> 2.02-2mdk
- disable suggests for now

* Tue Mar 14 2006 Götz Waschk <waschk@mandriva.org> 2.02-1mdk
- add audacious plugin
- New release 2.02

* Fri Jan 13 2006 Götz Waschk <waschk@mandriva.org> 2.01-1mdk
- suggest mod2ogg deps
- add mod2ogg
- New release 2.01

* Thu Jan 05 2006 Götz Waschk <waschk@mandriva.org> 2.00-3mdk
- fix dir on x86_64

* Sun Jan 01 2006 Götz Waschk <waschk@mandriva.org> 2.00-2mdk
- fix data dir

* Sun Jan 01 2006 Götz Waschk <waschk@mandriva.org> 2.00-1mdk
- drop audacious plugin
- drop patch
- new URL
- New release 2.00

* Fri Dec 02 2005 Götz Waschk <waschk@mandriva.org> 1.03-3mdk
- rebuild for audacious

* Fri Oct 28 2005 Lenny Cartier <lenny@mandriva.com> 1.03-2mdk
- rebuild for dependencies

* Tue Jul 26 2005 Götz Waschk <waschk@mandriva.org> 1.03-1mdk
- new version

* Tue May 24 2005 Götz Waschk <waschk@mandriva.org> 1.03-0.pre1.1mdk
- drop patch
- new version

* Tue May 10 2005 Götz Waschk <waschk@mandriva.org> 1.02-2mdk
- patch for gcc 4

* Sat May 07 2005 Götz Waschk <waschk@mandriva.org> 1.02-1mdk
- New release 1.02

* Mon Mar 14 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.01-1mdk
- New release 1.01

* Sun Oct 31 2004 Götz Waschk <waschk@linux-mandrake.com> 1.00-1mdk
- new version

* Tue Sep 28 2004 Götz Waschk <waschk@linux-mandrake.com> 1.00-0.pre1.1mdk
- switch to libao output
- new version

* Thu Jul 29 2004 Götz Waschk <waschk@linux-mandrake.com> 0.91-1mdk
- new version

* Tue Jul 20 2004 Götz Waschk <waschk@linux-mandrake.com> 0.91-0.pre3.1mdk
- drop patch
- new version

* Sat Jul 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.91-0.pre2.1mdk
- use installed-docs
- patch for beep-media-player build
- add beep-media-player plugin
- new version

* Fri Jul 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.91-0.pre1.1mdk
- split out xmms plugin
- update docs list
- build with optimization flags
- new version

* Wed Jun 16 2004 Götz Waschk <waschk@linux-mandrake.com> 0.90-1mdk
- enable alsa
- new version

* Sat Apr 17 2004 Götz Waschk <waschk@linux-mandrake.com> 0.90-0.pre2.1mdk
- drop merged patch 0
- new version

* Fri Apr 09 2004 Götz Waschk <waschk@linux-mandrake.com> 0.90-0.pre1.1mdk
- enable parallel build
- add man page
- new version

