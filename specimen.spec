%define pre	rc3
%define over	0.5.2

Name: 	 	specimen
Summary: 	MIDI-controlled sampler
Version: 	%{over}%{pre}
Release: 	%{mkrel 1}
# From Debian, upstream died years ago - AdamW 2008/08
Source0:	%{name}_%{version}.orig.tar.gz
# Allow external CFLAGS - AdamW 2008/08
Patch0:		specimen-0.5.1-cflags.patch
# From Debian: fix build (libjack calls) and major bug - AdamW 2008/08
Patch1:		specimen-0.5.2rc3-debian.patch
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
BuildRequires:	lash-devel

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
%setup -q -n %{name}-%{over}-%{pre}
%patch0 -p1 -b .cflags
%patch1 -p1 -b .debian

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

