%define name uade
%define version 2.11
%define fname %name-%{version}
%define release %mkrel 1

Summary: Unix Amiga Delitracker Emulator
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://zakalwe.fi/uade/uade2/%{fname}.tar.bz2
URL: http://zakalwe.fi/uade/
License: GPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: fuse-devel
BuildRequires: libao-devel
#gw for mod2ogg
%if %mdkversion >= 200800
Suggests: vorbis-tools
Suggests: normalize
Suggests: flac
Suggests: lame
%endif

%description
Plays old amiga tunes with UAE emulation and cloned m68k-assembler
Amiga delitracker API. With cloned delitracker API you don't have to
port old players from Amiga, you can re-use old Deliplayers that use
Amiga Delitracker API. Deliplayers are used like on Amiga, they exist
in some directory and you can copy/remove them as you wish. "Installing"
new players is just copying files to your 'players' directory.

%package -n xmms-uade
Group: Sound
Summary: Unix Amiga Delitracker Emulator Xmms input plugin
BuildRequires: libxmms-devel
Requires: xmms
Requires: uade = %version

%description -n xmms-uade
Plays old amiga tunes with UAE emulation and cloned m68k-assembler
Amiga delitracker API. With cloned delitracker API you don't have to
port old players from Amiga, you can re-use old Deliplayers that use
Amiga Delitracker API. Deliplayers are used like on Amiga, they exist
in some directory and you can copy/remove them as you wish. "Installing"
new players is just copying files to your 'players' directory.

This is the input plugin for xmms based on uade.

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

%prep
%setup -q -n %fname
find songs -name CVS|xargs rm -rfv
chmod 644 songs/* AUTHORS ChangeLog
chmod 755 songs/
%build
export CFLAGS="%optflags"
./configure --prefix=%{_prefix} --libdir=%_libdir --package-prefix=%buildroot
%make

%install
rm -rf %buildroot
make install PACKAGEPREFIX=%buildroot BINDIR=%buildroot%_bindir DATADIR=%buildroot%_datadir/uade2 XMMSPLUGINDIR=%buildroot%_libdir/xmms/Input/ AUDACIOUSPLUGINDIR=%buildroot%_libdir/audacious/Input/
mv %buildroot%_bindir/mod2ogg2.sh %buildroot%_bindir/mod2ogg
%if %_lib != lib
mv %buildroot%_prefix/lib/pkgconfig %buildroot%_libdir
%endif

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%doc songs
%{_bindir}/uade123
%{_bindir}/uadefs
%_bindir/mod2ogg
%{_datadir}/uade2
%_prefix/lib/uade2/
%_libdir/pkgconfig/uade.pc
%_mandir/man1/uade123.1*
%_mandir/man1/uadefs.1*

%files -n xmms-uade
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/xmms/Input/libuade2.so
%{_bindir}/uadexmmsadd

%files -n audacious-uade
%defattr(-,root,root)
%doc ChangeLog
%{_libdir}/audacious/Input/libuade2.so
