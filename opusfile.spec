Name:		opusfile
Version:	0.4
Release:	5
Summary:	A high-level API for decoding and seeking within .opus files
Group:		System/Libraries
License:	BSD
URL:		http://www.opus-codec.org/
Source0:	http://downloads.xiph.org/releases/opus/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ogg) >= 1.3
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(opus) >= 1.0.1

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

%define major 0
%define libname %mklibname %name %major

%package -n %libname
Summary: A high-level API for decoding and seeking within .opus files
Group: System/Libraries

%description -n %libname
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

%define develname %mklibname -d %{name}

%package -n %{develname}
Summary: Development package for %{name}
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}

%description -n %{develname}
Files for development with %{name}.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files -n %{libname}
%doc COPYING AUTHORS
%{_libdir}/libopus*.so.%{major}
%{_libdir}/libopus*.so.%{major}.*

%files -n %{develname}
%doc %{_docdir}/%{name}
%{_includedir}/opus/opusfile*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/libopus*.so
