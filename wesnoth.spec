# TODO add a init file for server, if it is worth
# split data if we can force a rpm to be noarch

Summary: Fantasy turn-based strategy game
Name: wesnoth
Version: 1.8.6
Release: %mkrel 1
License: GPLv2+
Group: Games/Strategy
Url: http://www.wesnoth.org/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1: %{name}-icon.png
BuildRequires: SDL_image-devel
BuildRequires: SDL_ttf-devel
BuildRequires: SDL_net-devel
BuildRequires: SDL_mixer-devel
BuildRequires: boost-devel
BuildRequires: oggvorbis-devel
BuildRequires: imagemagick
BuildRequires: python-devel
BuildRequires: pango-devel
BuildRequires: lua-devel >= 5.1.4
BuildRequires: cmake
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which
have advantages and disadvantages in different types of terrains and
against different types of attacks. Units gain experience and advance
levels, and are carried over from one scenario to the next campaign.

%package -n %{name}-server
Summary: Server for "Battle fo Wesnoth" game
Group: Games/Strategy

%description -n	%{name}-server
This package contains "Battle for wesnoth" server, used to play multiplayer
game without needing to install the full client.

%prep
%setup -q

%build
%cmake -DENABLE_STRICT_COMPILATION=OFF \
	-DBINDIR=%{_gamesbindir} \
	-DDATAROOTDIR=%{_gamesdatadir} \
	-DDESKTOPDIR=%{_datadir}/applications \
	-DDOCDIR=%{_datadir}/doc/%{name} \
	-DMANDIR=%{_mandir} -DICONDIR=%{_iconsdir}
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

%find_lang %{name} --all-name

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc README
%exclude %{_gamesbindir}/%{name}d
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_mandir}/*/%{name}.*
#%{_mandir}/*/%{name}_editor.*
#%lang(ca) %{_mandir}/ca_ES@valencia/*/%{name}.*
%lang(cs) %{_mandir}/cs/*/%{name}.*
#%lang(da) %{_mandir}/da/*/%{name}.*
%lang(de) %{_mandir}/de/*/%{name}.*
%lang(en) %{_mandir}/en_GB/*/%{name}.*
%lang(es) %{_mandir}/es/*/%{name}.*
%lang(et) %{_mandir}/et/*/%{name}.*
%lang(fi) %{_mandir}/fi/*/%{name}.*
%lang(fr) %{_mandir}/fr/*/%{name}.*
%lang(gl) %{_mandir}/gl/*/%{name}.*
%lang(hu) %{_mandir}/hu/*/%{name}.*
%lang(id) %{_mandir}/id/*/%{name}.*
%lang(it) %{_mandir}/it/*/%{name}.*
%lang(ja) %{_mandir}/ja/*/%{name}.*
%lang(lt) %{_mandir}/lt/*/%{name}.*
#%lang(nl) %{_mandir}/nl/*/%{name}.*
%lang(pl) %{_mandir}/pl/*/%{name}.*
%lang(pt) %{_mandir}/pt_BR/*/%{name}.*
#%lang(ca) %{_mandir}/racv/*/%{name}.*
%lang(sk) %{_mandir}/sk/*/%{name}.*
%lang(sr) %{_mandir}/sr/*/%{name}.*
%lang(sr@latin) %{_mandir}/sr@latin/*/%{name}.*
%lang(sr@ijekavian) %{_mandir}/sr@ijekavian/*/%{name}.*
%lang(sr@ijekavianlatin) %{_mandir}/sr@ijekavianlatin/*/%{name}.*
#lang(sv) %{_mandir}/sv/*/%{name}.*
%lang(tr) %{_mandir}/tr/*/%{name}.*
#lang(ru) %{_mandir}/ru/*/%{name}.*
%lang(zh_CN) %{_mandir}/zh_CN/*/%{name}.*
%lang(zh_TW) %{_mandir}/zh_TW/*/%{name}.*
%{_datadir}/applications/*
%{_iconsdir}/*

%files -n %{name}-server
%defattr(-,root,root,0755)
%{_gamesbindir}/%{name}d
%{_mandir}/*/%{name}d.*
#%lang(ca) %{_mandir}/ca_ES@valencia/*/%{name}d.*
%lang(cs) %{_mandir}/cs/*/%{name}d.*
#%lang(da) %{_mandir}/da/*/%{name}d.*
%lang(de) %{_mandir}/de/*/%{name}d.*
%lang(en) %{_mandir}/en_GB/*/%{name}d.*
%lang(es) %{_mandir}/es/*/%{name}d.*
%lang(et) %{_mandir}/et/*/%{name}d.*
%lang(fi) %{_mandir}/fi/*/%{name}d.*
%lang(fr) %{_mandir}/fr/*/%{name}d.*
%lang(gl) %{_mandir}/gl/*/%{name}d.*
%lang(hu) %{_mandir}/hu/*/%{name}d.*
%lang(id) %{_mandir}/id/*/%{name}d.*
%lang(it) %{_mandir}/it/*/%{name}d.*
%lang(ja) %{_mandir}/ja/*/%{name}d.*
%lang(lt) %{_mandir}/lt/*/%{name}d.*
#%lang(nl) %{_mandir}/nl/*/%{name}d.*
%lang(pl) %{_mandir}/pl/*/%{name}d.*
%lang(pt) %{_mandir}/pt_BR/*/%{name}d.*
#%lang(ca) %{_mandir}/racv/*/%{name}d.*
%lang(sk) %{_mandir}/sk/*/%{name}d.*
%lang(sr) %{_mandir}/sr/*/%{name}d.*
%lang(sr@latin) %{_mandir}/sr@latin/*/%{name}d.*
%lang(sr@ijekavian) %{_mandir}/sr@ijekavian/*/%{name}d.*
%lang(sr@ijekavianlatin) %{_mandir}/sr@ijekavianlatin/*/%{name}d.*
#lang(sv) %{_mandir}/sv/*/%{name}d.*
%lang(tr) %{_mandir}/tr/*/%{name}d.*
#lang(ru) %{_mandir}/ru/*/%{name}d.*
%lang(zh_CN) %{_mandir}/zh_CN/*/%{name}d.*
%lang(zh_TW) %{_mandir}/zh_TW/*/%{name}d.*

