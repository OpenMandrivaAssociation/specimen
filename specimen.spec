%define name	specimen
%define version	0.5.1
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	MIDI-controlled sampler
Version: 	%{version}
Release: 	%{release}

Source:		http://www.gazuga.net/files/%{name}-%{version}.tar.bz2
URL:		http://www.gazuga.net/
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig
BuildRequires:	gtk-devel libsamplerate-devel libxml2-devel
BuildRequires:	libalsa-devel jackit-devel ladcca-devel
BuildRequires:	phat-devel >= 0.3.1
BuildRequires:  libsndfile-devel

%description
A software sampler with:
- ALSA sequencer interface support
- audio output via ALSA or JACK
- individual panning and volume controls for each patch
- high quality cubically interpolated pitch scaling
- sample start/stop and loop points
- three playback modes; "normal" just plays the sample, "trim" plays the
  sample and stops early if so instructed, "loop" plays the sample for the
  requested duration
- patch bank saving and loading in the "beef" file format
- a waveform display

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=Specimen
Comment=MIDI software sampler
Categories=Audio;
EOF

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%name.desktop

