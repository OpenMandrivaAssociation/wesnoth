#Disable LTO on i686 and armv7 due to build fail because lack of memory (penguin).
%ifarch %{ix86} %{arm}
%define _disable_lto 1
%endif

# TODO add a init file for server, if it is worth
# split data if we can force a rpm to be noarch

%define sname wesnoth

Summary:	Fantasy turn-based strategy game
Name:		wesnoth
Version:	1.18.4
Release:	3
License:	GPLv2+
Group:		Games/Strategy
Url:		https://www.wesnoth.org/
# Looks like source from GH no longer contains lua submodules. Use tarball from wesnoth website instead.
#Source0:	https://github.com/wesnoth/wesnoth/archive/%{version}/%{sname}-%{version}.tar.gz
Source0:	https://www.wesnoth.org/files/wesnoth-%{version}.tar.bz2
Source1:	%{sname}-icon.png

BuildRequires:	cmake ninja
BuildRequires:	imagemagick
BuildRequires:	boost-devel
BuildRequires:	readline-devel
BuildRequires:  pkgconfig(libcurl)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_net)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
Conflicts:	%{sname}-unstable
Obsoletes:	wesnoth =< 1.17.0-2

%patchlist
wesnoth-1.18.3-boost-1.88.patch

%description
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which
have advantages and disadvantages in different types of terrains and
against different types of attacks. Units gain experience and advance
levels, and are carried over from one scenario to the next campaign.

%files -f %{sname}.lang
%exclude %{_bindir}/%{sname}d
%{_bindir}/*
%{_datadir}/%{sname}
%{_mandir}/*/%{sname}.*
%{_datadir}/applications/*
%{_datadir}/doc/%{sname}/*
%{_iconsdir}/*
%{_datadir}/metainfo/org.wesnoth.Wesnoth.appdata.xml

#----------------------------------------------------------------------------

%package -n %{name}-server
Summary:	Server for "Battle fo Wesnoth" game
Group:		Games/Strategy
Conflicts:	%{sname}-unstable-server

%description -n %{name}-server
This package contains "Battle for wesnoth" server, used to play multiplayer
game without needing to install the full client.

%files -n %{name}-server -f %{sname}d.lang
%{_bindir}/%{sname}d
%{_mandir}/*/%{sname}d.*

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{sname}-%{version}
find . -name ".gitignore" -delete

%cmake \
	-DENABLE_STRICT_COMPILATION=OFF \
	-DENABLE_SHARED_LIBRARIES=OFF \
	-DBINDIR=%{_bindir} \
	-DDATAROOTDIR=%{_datadir} \
	-DDESKTOPDIR=%{_datadir}/applications \
	-DDOCDIR=%{_datadir}/doc/%{sname} \
	-DMANDIR=%{_mandir} -DICONDIR=%{_iconsdir} \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{sname} --with-man
%find_lang %{sname}d --with-man
