%define major 0
%define libname %mklibname %{name} %{major}
%define liburl %mklibname opusurl %{major}
%define devname %mklibname %{name} -d

Summary:	A high-level API for decoding and seeking within .opus files
Name:		opusfile
Version:	0.12
Release:	2
License:	BSD
Group:		System/Libraries
Url:		http://www.opus-codec.org/
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(opus)

%description
libopusfile provides a high-level API for decoding and seeking
within .opus files. It includes:
* Support for all files with at least one Opus stream (including
multichannel files or Ogg files where Opus is muxed with something else).
* Full support, including seeking, for chained files.
* A simple stereo downmixing API (allowing chained files to be
decoded with a single output format, even if the channel count changes).
* Support for reading from a file, memory buffer, or over HTTP(S)
(including seeking).
* Support for both random access and streaming data sources.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%doc COPYING AUTHORS
%{_libdir}/libopusfile.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{liburl}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}opusfile0 < 0.6

%description -n %{liburl}
Shared library for %{name}.

%files -n %{liburl}
%{_libdir}/libopusurl.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development package for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{liburl} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Files for development with %{name}.

%files -n %{devname}
%doc %{_docdir}/%{name}
%{_includedir}/opus/opusfile*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libopus*.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install

