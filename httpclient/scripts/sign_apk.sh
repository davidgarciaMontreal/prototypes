#!/usr/bin/env bash

expandPath() {
  local path
  local -a pathElements resultPathElements
  IFS=':' read -r -a pathElements <<<"$1"
  : "${pathElements[@]}"
  for path in "${pathElements[@]}"; do
    : "$path"
    case ${path} in
      "~+"/*)
        path=$PWD/${path#"~+/"}
        ;;
      "~-"/*)
        path=$OLDPWD/${path#"~-/"}
        ;;
      "~"/*)
        path=$HOME/${path#"~/"}
        ;;
      "~"*)
        username=${path%%/*}
        username=${username#"~"}
        IFS=: read _ _ _ _ _ homedir _ < <(getent passwd "$username")
        if [[ ${path} = */* ]]; then
          path=${homedir}/${path#*/}
        else
          path=${homedir}
        fi
        ;;
    esac
    resultPathElements+=( "$path" )
  done
  local result
  printf -v result '%s:' "${resultPathElements[@]}"
  printf '%s\n' "${result%:}"
}

function create_key_store() {
    # Generate keystore to be use later to sign the APK
    pushd ~/
    valDays=10000
    keyalg="RSA"
    keytool -genkey -v -keystore ${keystore_location} \
            -alias ${alias_name_var} \
            -keyalg ${keyalg} -validity ${valDays}
    popd
}

keystore_location=$(expandPath '~/my-release-key.keystore')
alias_name_var="alias_name"

if [ ! -e ${keystore_location} ];then
    echo "Need to setup the keystore"
    echo "default location: ~/${keystore_location}"
    create_key_store
fi

# TODO: user input validation
if [ -z "$1" ];then
    echo "Usage:"
    echo "$BASH_SOURCE /path/to/android_app.apk"
    exit 1
fi
dir=$(dirname $1)
echo "Signing the apk file"
pushd ${dir}
jarsigner -verbose -keystore ${keystore_location} "$1" ${alias_name_var}
rc=$?
popd

[ ${rc} -ne 0 ] && echo "jarsigner failed with return code ${rc}" && exit ${rc} || echo "Signing the apk file is completed"