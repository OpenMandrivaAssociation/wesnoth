# TODO add a init file for server, if it is worth
# split data if we can force a rpm to be noarch

Summary:	Fantasy turn-based strategy game
Name:		wesnoth
Version:	1.10.5
Release:	1
License:	GPLv2+
Group:		Games/Strategy
Url:		http://www.wesnoth.org/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-icon.png
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_net-devel
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	imagemagick
BuildRequires:	python-devel
BuildRequires:	pkgconfig(lua)
BuildRequires:	cmake
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(fribidi)
Obsoletes:	wesnoth-unstable < %{version}

%description
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which
have advantages and disadvantages in different types of terrains and
against different types of attacks. Units gain experience and advance
levels, and are carried over from one scenario to the next campaign.

%package -n	%{name}-server
Summary:	Server for "Battle fo Wesnoth" game
Group:		Games/Strategy
Obsoletes:	wesnoth-unstable-server < %{version}

%description -n	%{name}-server
This package contains "Battle for wesnoth" server, used to play multiplayer
game without needing to install the full client.

%prep
%setup -q

%build
export LDFLAGS="$LDFLAGS -lpthread"
%cmake -DENABLE_STRICT_COMPILATION=OFF \
	-DBINDIR=%{_gamesbindir} \
	-DDATAROOTDIR=%{_gamesdatadir} \
	-DDESKTOPDIR=%{_datadir}/applications \
	-DDOCDIR=%{_datadir}/doc/%{name} \
	-DMANDIR=%{_mandir} -DICONDIR=%{_iconsdir}
%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-man
%find_lang %{name}d --with-man

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc README
%exclude %{_gamesbindir}/%{name}d
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_mandir}/*/%{name}.*
%{_datadir}/applications/*
%{_iconsdir}/*

%files -n %{name}-server -f %{name}d.lang
%defattr(-,root,root,0755)
%{_gamesbindir}/%{name}d
%{_mandir}/*/%{name}d.*

