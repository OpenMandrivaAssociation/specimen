%define name	specimen
%define version	0.5.1
%define release %mkrel 3

Name: 	 	specimen
Summary: 	MIDI-controlled sampler
Version: 	0.5.1
Release: 	%{mkrel 3}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		specimen-0.5.1-cflags.patch
License:	GPL+
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pkgconfig
BuildRequires:	gtk2-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libxml2-devel
BuildRequires:	libalsa-devel
BuildRequires:	jackit-devel
BuildRequires:	ladcca-devel
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
%patch0 -p1 -b .cflags

%build
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

#menu
mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{name}
Icon=sound_section
Name=Specimen
Comment=MIDI software sampler
Categories=GTK;Audio;
EOF

%find_lang %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

