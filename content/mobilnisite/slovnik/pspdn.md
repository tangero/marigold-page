---
slug: "pspdn"
url: "/mobilnisite/slovnik/pspdn/"
type: "slovnik"
title: "PSPDN – Packet Switched Public Data Network"
date: 2025-01-01
abbr: "PSPDN"
fullName: "Packet Switched Public Data Network"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pspdn/"
summary: "Veřejná síť, která poskytuje předplatitelům služby paketově přepínané datové komunikace. V kontextu 3GPP často označuje externí sítě, jako je internet nebo firemní intranety, ke kterým se zařízení mob"
---

PSPDN je veřejná paketově přepínaná datová síť, například internet nebo firemní intranet, ke které se mobilní uživatelé připojují přes páteřní síť mobilního operátora.

## Popis

Paketově přepínaná veřejná datová síť (PSPDN) je obecný telekomunikační termín přijatý v rámci 3GPP pro označení jakékoli veřejné síťové infrastruktury, která nabízí služby přenosu dat pomocí technologie paketového přepínání. Na rozdíl od přepojování okruhů, které je vyhrazeno pro hlas, PSPDN rozděluje data na pakety, které jsou v síti směrovány nezávisle. V architektuře sítí 2G ([GPRS](/mobilnisite/slovnik/gprs/)), 3G a vyvinutého paketového jádra (EPC) představuje PSPDN externí cílovou datovou síť. Páteřní síť mobilního operátora funguje jako přístupová brána, která připojuje mobilního předplatitele k této externí PSPDN.

Připojení zprostředkovávají specifické uzly-brány uvnitř mobilního jádra. V sítích GPRS 2G/3G slouží uzel Gateway GPRS Support Node (GGSN) jako rozhraní mezi mobilním paketovým jádrem a externími PSPDN. Ve 4G EPC a 5G Core (5GC) plní podobnou roli uzel Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) a funkce User Plane Function ([UPF](/mobilnisite/slovnik/upf/)). Když mobilní zařízení aktivuje kontext Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) nebo naváže Protocol Data Unit ([PDU](/mobilnisite/slovnik/pdu/)) Session pro přístup na internet, v podstatě žádá o připojení ke konkrétní PSPDN, která je často identifikována názvem přístupového bodu ([APN](/mobilnisite/slovnik/apn/)). Uzel-brána spravuje přidělování IP adresy uživatele, provádí směrování IP paketů mezi mobilní sítí a PSPDN a vynucuje pravidla pro politiky a účtování.

Samotná PSPDN je z velké části mimo rozsah standardizace 3GPP, protože se jedná o externí síť. Specifikace 3GPP definují, jak se k ní mobilní síť připojuje. PSPDN může být veřejný internet, privátní firemní síť nebo síť poskytovatele internetových služeb ([ISP](/mobilnisite/slovnik/isp/)). Mobilní síť poskytuje k této síti 'přístupovou' službu. Mezi klíčové zapojené protokoly patří IP na síťové vrstvě a uzly-brány implementují na hranici mezi důvěryhodnou mobilní doménou a externí PSPDN funkce jako firewall, hluboká kontrola paketů (DPI) a tvarování provozu. Tento koncept je základní pro nabídku datových služeb jakéhokoli mobilního operátora.

## K čemu slouží

Koncept PSPDN byl nedílnou součástí vývoje mobilních datových služeb počínaje [GPRS](/mobilnisite/slovnik/gprs/) v sítích 2G. Jeho účelem bylo formálně definovat cíl pro mobilní datový provoz, oddělit odpovědnost mobilního operátora za přístup a páteřní přenos od služeb poskytovaných externími datovými sítěmi. Před rozšířením paketových dat byly mobilní sítě primárně okruhově přepínané pro hlas, s omezenými proprietárními datovými schopnostmi. Model PSPDN uznal, že hodnota mobilních dat spočívá v připojení k existujícím rozsáhlým paketovým sítím, jako je internet.

Toto oddělení vyřešilo klíčové architektonické a obchodní problémy. Umožnilo operátorům mobilních sítí zaměřit se na poskytování spolehlivého, fakturovatelného přístupu a správy mobility, aniž by se sami museli stát poskytovateli obsahu nebo aplikací. Umožnilo jasné vymezení hranice pro účtování, zabezpečení a vynucování politik. Uzel-brána (GGSN/PGW) se stal místem vynucování politik mezi řízenou sítí operátora a nedůvěryhodnou PSPDN. Tento model umožnil explozivní růst mobilního internetu, protože uživatelé mohli ze svých mobilních zařízení přistupovat ke stejným internetovým službám jako z pevných linek. PSPDN zůstává základním konceptem i v 5G, kde je analogickým termínem 'Datová síť' (DN), což zdůrazňuje pokračující architektonický princip připojování mobilních uživatelů k externím paketovým službám.

## Klíčové vlastnosti

- Externí cílová síť pro mobilní datové relace (např. internet)
- Připojena přes uzly-brány (GGSN, PGW, UPF) v mobilním jádru
- Identifikována názvem přístupového bodu (APN) při navazování relace
- Pro přenos dat používá standardní internetový protokol (IP)
- Hraniční bod pro politiky operátora, účtování a bezpečnostní kontroly
- Základní pro architekturu mobilních paketových datových služeb od 2G do 5G

## Související pojmy

- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification

---

📖 **Anglický originál a plná specifikace:** [PSPDN na 3GPP Explorer](https://3gpp-explorer.com/glossary/pspdn/)
