---
slug: "hnb-gw"
url: "/mobilnisite/slovnik/hnb-gw/"
type: "slovnik"
title: "HNB-GW – Home Node B Gateway"
date: 2025-01-01
abbr: "HNB-GW"
fullName: "Home Node B Gateway"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/hnb-gw/"
summary: "HNB-GW (brána pro Home Node B) je síťový prvek, který agreguje a zabezpečuje připojení od mnoha Home Node B (femtobuněk) přes veřejný internet. K jádru sítě prezentuje standardní rozhraní Iu, čímž skr"
---

HNB-GW je síťový prvek, který agreguje a zabezpečuje připojení od mnoha Home Node B přes veřejný internet a poskytuje standardní rozhraní Iu k jádru sítě.

## Popis

HNB-GW (Home Node B Gateway) je klíčová agregační a zabezpečovací brána v architektuře femtobuněk ([HNB](/mobilnisite/slovnik/hnb/)) 3GPP UMTS. Jejím hlavním úkolem je sloužit jako síťový koncový bod pro zabezpečené tunely založené od tisíců distribuovaných Home Node B (HNB) přes nedůvěryhodné IP sítě (jako je veřejný internet). Z pohledu prvků jádra sítě – Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) pro okruhově spínané hovory a Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) pro paketová data – se HNB-GW jeví jako standardní Radio Network Controller ([RNC](/mobilnisite/slovnik/rnc/)), komunikující prostřednictvím rozhraní Iu-CS, resp. Iu-PS.

Operačně každá HNB objeví a zaregistruje se u HNB-GW, čímž založí zabezpečený [IPsec](/mobilnisite/slovnik/ipsec/) tunel pro veškerý řídicí a uživatelský provoz. HNB-GW autentizuje HNB, často pomocí certifikátů, a spravuje životní cyklus tohoto zabezpečeného spojení. Ukončuje rozhraní Iu-h od HNB, které nese modifikovanou verzi protokolu [RANAP](/mobilnisite/slovnik/ranap/), a překládá jej do standardní signalizace rozhraní Iu pro jádro sítě. To zahrnuje přenos aktualizací polohy, požadavků na zřízení hovoru a zpráv o předání spojení. V uživatelské rovině může HNB-GW provádět funkce koncentrace a zákonného odposlechu, přeposílaje hlasové a datové pakety mezi zabezpečeným tunelem a mediálními bránami nebo GGSN jádra sítě.

HNB-GW také hraje klíčovou roli v řízení mobility. Zpracovává předání spojení mezi HNB pod její kontrolou (intra-HNB-GW handover) a může usnadňovat předání spojení do makro sítě UMTS a z ní. Udržuje kontext pro aktivní UE připojená přes HNB. Dále komunikuje se systémem pro správu HNB ([HMS](/mobilnisite/slovnik/hms/)) kvůli provisioning a správě poruch HNB. Koncentrací provozu od mnoha nízkokapacitních HNB poskytuje HNB-GW škálovatelnou architekturu, která chrání jádro sítě před přímou expozicí obrovskému množství spotřebitelských zařízení.

## K čemu slouží

HNB-GW byla vytvořena, aby řešila zásadní výzvy síťové integrace a zabezpečení spojené s masovým nasazením spotřebitelských femtobuněk (HNB). Bez brány by se každá HNB musela připojovat přímo k uzlům jádra sítě operátora (MSC, SGSN), což nebylo škálovatelné ani bezpečné přes veřejný internet. HNB-GW poskytuje nezbytnou agregační hranici a hranici důvěry.

Řeší několik klíčových problémů: Zabezpečení, ukončováním IPsec tunelů a autentizací HNB před tím, než získají přístup k prostředkům jádra sítě; Škálovatelnost, agregací signalizace a provozu od potenciálně milionů HNB do spravovatelného počtu rozhraní směrem k jádru; a Transparentnost, skrytím aspektů specifických pro femtobuňky (jako je rozhraní Iu-h a správa CSG) před starším jádrem sítě, což umožňuje existujícím MSC a SGSN fungovat bez větších upgradů.

Vývoj HNB-GW ve verzi Release 8 byl motivován potřebou standardizované, operátorské architektury, která by umožnila operátorům bezpečně a efektivně nasazovat femtobuňky ve velkém měřítku. Poskytla klíčový kus infrastruktury, který učinil obchodní model rezidenčních femtobuněk životaschopným, zajistila integritu sítě, umožnila efektivní využití zdrojů a podporovala nezbytné funkce jako mobilita a zákonný odposlech.

## Klíčové vlastnosti

- Agreguje řídicí a uživatelská připojení od velkého počtu HNB
- Ukončuje zabezpečené IPsec tunely od HNB přes nedůvěryhodné IP sítě
- Působí jako koncentrátor a prezentuje standardní rozhraní Iu k jádru sítě (MSC, SGSN)
- Překládá mezi protokolem specifickým pro HNB na rozhraní Iu-h a standardním RANAP na rozhraní Iu
- Spravuje registraci, autentizaci a bezpečnostní kontext HNB
- Zpracovává mobilitu, včetně předání spojení mezi HNB a do/z makro sítě

## Související pojmy

- [HNB – Home Node B](/mobilnisite/slovnik/hnb/)
- [RANAP – Radio Access Network Application Protocol](/mobilnisite/slovnik/ranap/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)

## Definující specifikace

- **TS 25.444** (Rel-19) — HNB User Data Transport Protocols
- **TS 25.467** (Rel-19) — UTRAN Architecture for 3G Home Node B
- **TS 25.468** (Rel-19) — RANAP User Adaption (RUA) protocol specification
- **TS 25.469** (Rel-19) — HNBAP Specification for HNB to HNB-GW Interface
- **TS 25.470** (Rel-19) — PCAP User Adaption (PUA) protocol specification
- **TR 25.967** (Rel-19) — Home NodeB RF Requirements Technical Report
- **TS 28.673** (Rel-19) — HNS NRM IRP Solution Set Definitions
- **TS 31.104** (Rel-19) — HPSIM Application Specification
- **TS 32.583** (Rel-19) — HNB OAM&P Procedure Flows for Type 1 Interface
- **TS 32.821** (Rel-9) — SON OAM Architecture for Home NodeB

---

📖 **Anglický originál a plná specifikace:** [HNB-GW na 3GPP Explorer](https://3gpp-explorer.com/glossary/hnb-gw/)
