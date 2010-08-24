# TODO add a init file for server, if it is worth
# split data if we can force a rpm to be noarch

Summary: Fantasy turn-based strategy game
Name: wesnoth
Version: 1.8.4
Release: %mkrel 2
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
	-DDOCDIR=%{_datadir}/doc/%name \
	-DMANDIR=%{_mandir} -DICONDIR=%{_iconsdir}
%make

%install

rm -rf $RPM_BUILD_ROOT

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
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc README
%exclude %{_gamesbindir}/%{name}d
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_mandir}/*/%{name}.*
#%{_mandir}/*/%{name}_editor.*
#%lang(ca) %{_mandir}/ca_ES@valencia/*/*
%lang(cs) %{_mandir}/cs/*/*
#%lang(da) %{_mandir}/da/*/*
%lang(de) %{_mandir}/de/*/*
%lang(en) %{_mandir}/en_GB/*/*
%lang(es) %{_mandir}/es/*/*
%lang(et) %{_mandir}/et/*/*
%lang(fi) %{_mandir}/fi/*/*
%lang(fr) %{_mandir}/fr/*/*
%lang(gl) %{_mandir}/gl/*/*
%lang(hu) %{_mandir}/hu/*/*
%lang(it) %{_mandir}/it/*/*
%lang(ja) %{_mandir}/ja/*/*
%lang(lt) %{_mandir}/lt/*/*
#%lang(nl) %{_mandir}/nl/*/*
%lang(pl) %{_mandir}/pl/*/*
%lang(pt) %{_mandir}/pt_BR/*/*
#%lang(ca) %{_mandir}/racv/*/*
%lang(sk) %{_mandir}/sk/*/*
%lang(sr) %{_mandir}/sr/*/*
%lang(sr@latin) %{_mandir}/sr@latin/*/*
%lang(sr@ijekavian) %{_mandir}/sr@ijekavian/*/*
%lang(sr@ijekavianlatin) %{_mandir}/sr@ijekavianlatin/*/*
#lang(sv) %{_mandir}/sv/*/*
%lang(tr) %{_mandir}/tr/*/*
#lang(ru) %{_mandir}/ru/*/*
%lang(zh_CN) %{_mandir}/zh_CN/*/*
%lang(zh_TW) %{_mandir}/zh_TW/*/*
%{_datadir}/applications/*
%{_iconsdir}/*

%files -n %{name}-server
%defattr(-,root,root,0755)
%{_gamesbindir}/%{name}d
%{_mandir}/*/%{name}d.*
