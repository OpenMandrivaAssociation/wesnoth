# TODO add a init file for server, if it is worth
# split data if we can force a rpm to be noarch

Summary: Fantasy turn-based strategy game
Name: wesnoth
Version: 1.6.5
Release: %mkrel 4
License: GPLv2+
Group: Games/Strategy
Url: http://www.wesnoth.org/
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1: %{name}-icon.png
Patch0: wesnoth-0.9.0-fix-non-root-install.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: SDL_image-devel
BuildRequires: SDL_ttf-devel
BuildRequires: SDL_net-devel
BuildRequires: SDL_mixer-devel
BuildRequires: boost-devel
BuildRequires: oggvorbis-devel
BuildRequires: imagemagick
BuildRequires: python-devel
BuildRequires: pango-devel

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
#%patch0 -p1 -b .nonroot

%build
export CFLAGS="%optflags -fno-strict-aliasing"
export CXXFLAGS=$CFLAGS

%configure --datadir=%{_gamesdatadir} \
 --bindir=%{_gamesbindir} \
 --enable-server \
 --enable-editor \
 --enable-python \
 --with-localedir=%{_datadir}/locale \
 --disable-strict-compilation
#perl -pi -e 's|^localedir = .*|localedir=%{_datadir}/locale|' $(find . -name Makefile )
%make

%install

rm -rf $RPM_BUILD_ROOT

%makeinstall_std
mkdir -p $RPM_BUILD_ROOT{%{_miconsdir},%{_iconsdir},%{_liconsdir}}

cp %{SOURCE1} $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png -size 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png -size 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png


# menu entry

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Battle For Wesnoth
Comment=A fantasy turn-based strategy game.
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Strategy;Game;StrategyGame;
EOF

cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}-editor.desktop << EOF
[Desktop Entry]
Name=Battle For Wesnoth editor
Comment=The map editor of Battle for Wesnoth
Exec=%_gamesbindir/%{name}_editor
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Strategy;Game;StrategyGame;
EOF

#remove desktop and icons installed in _gamesdatadir
rm -rf %{buildroot}%{_gamesdatadir}/applications
rm -rf %{buildroot}%{_gamesdatadir}/icons

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
%{_liconsdir}/%{name}.*
%{_iconsdir}/%{name}.*
%{_miconsdir}/%{name}.*
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
#%lang(ja) %{_mandir}/ja/*/*
%lang(lt) %{_mandir}/lt/*/*
#%lang(nl) %{_mandir}/nl/*/*
%lang(pl) %{_mandir}/pl/*/*
#lang(pt) %{_mandir}/pt_BR/*/*
#%lang(ca) %{_mandir}/racv/*/*
%lang(sk) %{_mandir}/sk/*/*
%lang(sr) %{_mandir}/sr/*/*
%lang(sr@latin) %{_mandir}/sr@latin/*/*
%lang(sv) %{_mandir}/sv/*/*
%lang(tr) %{_mandir}/tr/*/*
#lang(ru) %{_mandir}/ru/*/*
%lang(zh_CN) %{_mandir}/zh_CN/*/*
%lang(zh_TW) %{_mandir}/zh_TW/*/*
%{_datadir}/applications/*

%files -n %{name}-server
%defattr(-,root,root,0755)
%{_gamesbindir}/%{name}d
%{_mandir}/*/%{name}d.*
