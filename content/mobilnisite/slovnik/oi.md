---
slug: "oi"
url: "/mobilnisite/slovnik/oi/"
type: "slovnik"
title: "OI – Operator Identifier"
date: 2025-01-01
abbr: "OI"
fullName: "Operator Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/oi/"
summary: "Jedinečný identifikátor operátora mobilní sítě, který tvoří část Názvu přístupového bodu (APN). Používá se v procesu připojení k paketové datové síti (PDN) ke směrování datového provozu uživatele do s"
---

OI je jedinečný identifikátor operátora mobilní sítě, který tvoří část APN a používá se ke směrování datového provozu uživatele do správné sítě operátora během připojení k PDN.

## Popis

Identifikátor operátora (OI) je základní součástí síťové architektury 3GPP, konkrétně v oblasti paketové datové konektivity. Jedná se o řetězec znaků, který jednoznačně identifikuje operátora mobilní sítě ([MNO](/mobilnisite/slovnik/mno/)) nebo virtuálního operátora mobilní sítě ([MVNO](/mobilnisite/slovnik/mvno/)) v globálním měřítku. Jeho primární technická role spočívá v tom, že je součástí Názvu přístupového bodu ([APN](/mobilnisite/slovnik/apn/)), což je plně kvalifikovaný doménový název ([FQDN](/mobilnisite/slovnik/fqdn/)) používaný uživatelským zařízením (UE) k navázání datového připojení ke konkrétní paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)), jako je internet nebo operátorova služba IMS.

APN je strukturován ze dvou hlavních částí: Identifikátoru sítě ([NI](/mobilnisite/slovnik/ni/)), který specifikuje externí PDN (např. 'internet'), a Identifikátoru operátora (OI), který specifikuje síť, ke které je připojení PDN ukotveno. Samotný OI má definovaný formát, který typicky sestává ze dvou nebo tří štítků. Pro domovskou síť často má podobu 'mnc<[MNC](/mobilnisite/slovnik/mnc/)>.mcc<[MCC](/mobilnisite/slovnik/mcc/)>.gprs', kde MNC je kód mobilní sítě a MCC je kód mobilní země přiřazený operátorovi. Tato struktura zajišťuje globální jedinečnost. Když UE požaduje připojení k PDN, může síti poskytnout APN. Obsluhující síť (SGSN v GPRS/UMTS, MME v LTE, AMF v 5G) tento APN parsuje, aby extrahovala OI.

Parsování a interpretace OI jsou klíčové pro rozhodování o směrování. Pokud se OI v požadovaném APN shoduje s identifikátorem domovské sítě, připojení je navázáno lokálně. Pokud odpovídá identifikátoru roamujícího partnera, může obsluhující síť směrovat žádost o připojení do sítě tohoto partnera prostřednictvím příslušných mezifunkčních rozhraní (např. GTP-C tunelů). Tento mechanismus je zásadní pro umožnění plynulých roamujících datových služeb. OI se také používá v interních síťových procesech, jako je překlad APN v systému doménových jmen (DNS) sítě operátora, kde pomáhá přeložit APN na IP adresu příslušné brány GPRS podpůrného uzlu (GGSN), brány paketové datové sítě (PGW) nebo funkce uživatelské roviny (UPF).

Kromě základní konektivity hraje OI roli v diferenciaci služeb a vynucování politik. Síťové politiky, definované v systémech jako funkce pravidel pro řízení a účtování (PCRF), mohou být vázány na APN (a tedy na OI) pro aplikaci specifických pravidel kvality služeb (QoS), účtování a řízení přístupu. To umožňuje operátorovi nabízet odlišné servisní profily pro různé partnerské sítě nebo pro své vlastní služby. V 5G se tento koncept vyvíjí s Názvem datové sítě (DNN), ale princip identifikace síťového operátora pro účely směrování a politik zůstává zásadně důležitý.

## K čemu slouží

Identifikátor operátora byl vytvořen k vyřešení základního problému jednoznačné identifikace sítě mobilního operátora v globálně propojeném ekosystému, zejména pro paketově přepínané datové služby. Před standardizovanými datovými službami roamování v okruhově přepínané hlasové službě spoléhalo na Mezinárodní identifikaci účastníka mobilní sítě (IMSI), která obsahuje MCC a MNC. Vzestup GPRS a paketových dat však přinesl potřebu logického směrovacího systému založeného na jménech – APN – pro nasměrování datových relací ke konkrétním servisním sítím (např. podniková intranet, WAP portál, veřejný internet). OI poskytuje zásadní 'operátorskou' část tohoto názvu.

Jeho vytvoření bylo motivováno potřebou škálovatelného a flexibilního datového roamování. Bez standardizovaného identifikátoru operátora uvnitř APN by navštívená síť nemohla určit, kam směrovat žádost o datovou relaci iniciovanou roamujícím účastníkem. OI, založený na globálně jedinečné dvojici MCC/MNC, poskytuje tento deterministický směrovací klíč. Umožňuje jakékoli síti na světě identifikovat domovského operátora (nebo konkrétního partnerského operátora) spojeného s požadovanou datovou službou a navázat příslušný tunel k bráně tohoto operátora.

Dále OI umožňuje operátorovi kontrolu nad vystavením služeb. Umožňuje operátorovi hostovat více logicky oddělených paketových datových sítí (např. 'internet.mnc01.mcc234.gprs' a 'ims.mnc01.mcc234.gprs') při použití stejné infrastruktury jádra sítě. To usnadňuje diferenciaci služeb a vytváření vyhrazených APN pro podnikové zákazníky nebo služby IoT. OI je v podstatě základním kamenem architektury APN, který umožňuje technickou realizaci obchodních a technických dohod mezi operátory v síti, podporujících jak roaming, tak komplexní servisní nabídky.

## Klíčové vlastnosti

- Globálně jedinečný identifikátor operátora mobilní sítě založený na MCC a MNC
- Povinná součást struktury Názvu přístupového bodu (APN)
- Používá se pro směrování žádostí o připojení k PDN v domácích i roamujících scénářích
- Umožňuje překlad APN v DNS infrastruktuře operátora
- Umožňuje výběr pravidel pro politiky a účtování na základě cílové sítě
- Podporuje diferenciaci služeb prostřednictvím operátorsky specifických APN

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [MCC – Mobile Country Code](/mobilnisite/slovnik/mcc/)
- [MNC – Mobile Network Code](/mobilnisite/slovnik/mnc/)
- [DNN – Data Network Name](/mobilnisite/slovnik/dnn/)

## Definující specifikace

- **TS 24.234** (Rel-12) — 3GPP-WLAN Interworking Network Selection
- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [OI na 3GPP Explorer](https://3gpp-explorer.com/glossary/oi/)
