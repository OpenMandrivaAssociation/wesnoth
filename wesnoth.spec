# TODO add a init file for server, if it is worth
# split data if we can force a rpm to be noarch

Summary:	Battle for Wesnoth is a fantasy turn-based strategy game
Name:		wesnoth
Version: 1.2.5
Release: %mkrel 1
License:	GPL
Group:		Games/Strategy
Url:		http://www.wesnoth.org/
Source0:	http://www.wesnoth.org/files/%{name}-%{version}.tar.bz2
Source1:	%{name}-icon.png
Patch0:		wesnoth-0.9.0-fix-non-root-install.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL_image-devel SDL_ttf-devel
BuildRequires:	SDL_net-devel SDL_mixer-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	ImageMagick
BuildRequires:	python-devel

%description
Battle for Wesnoth is a fantasy turn-based strategy game.
Battle for control of villages, using variety of units which 
have advantages and disadvantages in different types of terrains and 
against different types of attacks. Units gain experience and advance 
levels, and are carried over from one scenario to the next campaign.

%package -n	%{name}-server
Summary:	Server for "Battle fo Wesnoth" game 
Group:		Games/Strategy

%description -n	%{name}-server
This package contains "Battle for wesnoth" server, used to play multiplayer
game without needing to install the full client.


%prep
%setup -q
#%patch0 -p1 -b .nonroot
%build
%configure	--datadir=%{_gamesdatadir} \
		--bindir=%{_gamesbindir} \
		--enable-server \
		--enable-editor \
        --enable-python \
		--with-localedir=%{_datadir}/locale
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
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): \
needs="x11" \
section="More Applications/Games/Strategy" \
title="Battle For Wesnoth" \
longtitle="A fantasy turn-based strategy game." \
command="%{_gamesbindir}/%{name}" \
icon="%{name}.png" \
xdg="true"
?package(%{name}): \
needs="x11" \
section="More Applications/Games/Strategy" \
title="Battle For Wesnoth editor" \
longtitle="The map editor of Battle for Wesnoth" \
command="%{_gamesbindir}/%{name}_editor" \
icon="%{name}.png" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
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
Encoding=UTF-8
Name=Battle For Wesnoth editor
Comment=The map editor of Battle for Wesnoth
Exec=%_gamesbindir/%{name}_editor
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Strategy;Game;StrategyGame;
EOF

%find_lang %{name} --all-name

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc changelog MANUAL MANUAL.* README
%exclude %{_gamesbindir}/%{name}d
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_menudir}/%{name}
%{_liconsdir}/%{name}.*
%{_iconsdir}/%{name}.*
%{_miconsdir}/%{name}.*
%{_mandir}/*/%{name}.*
%{_mandir}/*/%{name}_editor.*
%lang(de) %{_mandir}/de/*/*
%lang(sv) %{_mandir}/sv/*/*
%lang(cs) %{_mandir}/cs/*/*
%lang(en) %{_mandir}/en_GB/*/*
%lang(cs) %{_mandir}/cs/*/*
%lang(fr) %{_mandir}/fr/*/*
%lang(it) %{_mandir}/it/*/*
%lang(ja) %{_mandir}/ja/*/*
%lang(nl) %{_mandir}/nl/*/*
%lang(pt) %{_mandir}/pt_BR/*/*
%lang(sk) %{_mandir}/sk/*/*
%lang(ru) %{_mandir}/ru/*/*
%{_datadir}/applications/*

%files -n %{name}-server
%defattr(-,root,root,0755)
%{_gamesbindir}/%{name}d
%{_mandir}/*/%{name}d.*


