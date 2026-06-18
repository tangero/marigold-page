---
slug: "napt-pt"
url: "/mobilnisite/slovnik/napt-pt/"
type: "slovnik"
title: "NAPT-PT – NAPT and Protocol Translation"
date: 2025-01-01
abbr: "NAPT-PT"
fullName: "NAPT and Protocol Translation"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/napt-pt/"
summary: "NAPT-PT kombinuje překlad síťových adres a portů (NAPT) s překladem protokolů mezi IPv4 a IPv6. Umožňuje komunikaci mezi sítěmi nebo aplikacemi pracujícími výhradně s IPv4 a IPv6 a funguje jako klíčov"
---

NAPT-PT je přechodový mechanismus, který kombinuje překlad síťových adres a portů (NAPT) s překladem protokolů (PT) za účelem umožnění komunikace mezi sítěmi nebo aplikacemi pracujícími výhradně s protokolem IPv4 a IPv6.

## Popis

[NAPT](/mobilnisite/slovnik/napt/) and Protocol Translation (NAPT-PT) je dvoufunkční síťový prvek specifikovaný 3GPP, který poskytuje dvě odlišné, ale související překladové služby. Za prvé provádí standardní NAPT, tedy překlad privátních IPv4 adres a portů na veřejnou IPv4 adresu a porty. Za druhé, a to je klíčové, provádí překlad protokolů ([PT](/mobilnisite/slovnik/pt/)), který konvertuje hlavičky a datovou část paketů mezi protokoly IPv4 a IPv6. To umožňuje, aby uživatelské zařízení (UE) nebo síťový segment pracující pouze s IPv6 komunikoval se serverem nebo službou pracujícími pouze s IPv4 ve vnější paketové datové síti ([PDN](/mobilnisite/slovnik/pdn/)), a naopak.

Komponenta pro překlad protokolů je založena na mechanismech definovaných ve standardech [IETF](/mobilnisite/slovnik/ietf/), jako je Stateless IP/[ICMP](/mobilnisite/slovnik/icmp/) Translation (SIIT) a její stavová rozšíření. Když paket IPv6 od UE určený pro hostitele IPv4 dorazí k funkci NAPT-PT, ta přeloží hlavičku IPv6 na hlavičku IPv4. To zahrnuje mapování zdrojové IPv6 adresy na IPv4 adresu z vyhrazeného fondu, úpravu délky paketu a překlad zpráv ICMPv6 na ICMPv4. Zásadní je také zpracování vložených IP adres v rámci některých protokolů aplikační vrstvy (např. [FTP](/mobilnisite/slovnik/ftp/), [SIP](/mobilnisite/slovnik/sip/)) pomocí aplikačních bran (ALG), aby bylo zajištěno kompletní propojení. Opačný proces se provádí pro provoz směřující z internetu IPv4 k uživatelskému zařízení IPv6.

Z architektonického hlediska je NAPT-PT pozicováno jako síťové řešení překladu, často umístěné společně s branou PDN ([PGW](/mobilnisite/slovnik/pgw/)) nebo podobným hraničním prvkem. Jeho činnost je stavová, udržuje vazební a relací tabulky, které korelují adresu/port IPv6 s přeloženou adresou/portem IPv4. To mu umožňuje správně směrovat zpětný provoz. Specifikace 3GPP podrobně popisují jeho integraci s řízením politik a účtováním, což operátorům umožňuje selektivně aplikovat NAPT-PT na základě profilu účastníka, APN nebo cílové služby. Kvůli významné technické složitosti a narušení sémantiky end-to-end IP se však jeho použití obecně považuje za přechodový nástroj poslední volby.

## K čemu slouží

NAPT-PT bylo vytvořeno k řešení kritického problému interoperability během dlouhého a asymetrického přechodu z IPv4 na IPv6. Když mobilní sítě začaly nasazovat IPv6 pro nová uživatelská zařízení (UE) a síťové domény, naprostá většina obsahu a služeb na internetu zůstávala pouze na IPv4. Přímá komunikační cesta mezi těmito dvěma nekompatibilními protokolovými světy byla bez překladu nemožná. NAPT-PT poskytlo síťový most, který umožnil časné přijetí IPv6 bez nutnosti okamžitého a univerzálního upgradu všech koncových bodů a serverů.

Řešilo to omezení nasazení duálního zásobníku (dual-stack), který vyžaduje přítomnost zásobníků IPv4 i IPv6 na všech zařízeních a sítích – což je nákladný a pomalý proces. NAPT-PT nabídlo přírůstkovější cestu, která operátorům umožnila nasadit přístupovou síť pouze s IPv6 pro nová UE, a zároveň zachovat přístup ke stávajícímu internetu IPv4. To bylo zvláště motivováno snahou šetřit ubývající adresní prostor IPv4; novým UE mohly být přidělovány pouze adresy IPv6, čímž se zabránilo spotřebě cenných veřejných IPv4 adres.

Tato technologie však byla koncipována jako přechodový mechanismus, nikoli jako trvalé řešení. Jejím účelem bylo umožnit koexistenci, nikoli nahradit nativní end-to-end komunikaci přes IPv6. IETF a později 3GPP uznaly významné nevýhody NAPT-PT, včetně složitosti, vytváření jednotných bodů selhání a nekompatibility s mnoha aplikacemi a bezpečnostními protokoly (jako je IPsec). To vedlo k jeho zavržení ve prospěch škálovatelnějších přechodových technologií, jako je 464XLAT a Dual-Stack Lite (DS-Lite), v pozdějších vydáních.

## Klíčové vlastnosti

- Provádí kombinovaný překlad síťových adres a portů (NAPT) a překlad protokolů IPv4/IPv6 (PT)
- Umožňuje obousměrnou komunikaci mezi uživatelskými zařízeními (UE) pouze s IPv6 a externími sítěmi/službami pouze s IPv4
- Obsahuje aplikační brány (ALG) pro protokoly, které vkládají IP adresy do datové části
- Funguje jako stavový překladač, který udržuje tabulky vazeb relací
- Integruje se s řízením politik 3GPP pro selektivní aplikaci na základě APN nebo účastníka
- Využívá fondy IPv4 adres pro mapování zdrojových IPv6 adres během překladu

## Definující specifikace

- **TS 29.238** (Rel-19) — H.248 Profile for IBCF-TrGW Interface
- **TS 29.334** (Rel-19) — IMS-ALG to IMS-AGW Interface Protocol

---

📖 **Anglický originál a plná specifikace:** [NAPT-PT na 3GPP Explorer](https://3gpp-explorer.com/glossary/napt-pt/)
