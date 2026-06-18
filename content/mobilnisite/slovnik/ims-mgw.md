---
slug: "ims-mgw"
url: "/mobilnisite/slovnik/ims-mgw/"
type: "slovnik"
title: "IMS-MGW – IP Multimedia Subsystem Media Gateway Function"
date: 2025-01-01
abbr: "IMS-MGW"
fullName: "IP Multimedia Subsystem Media Gateway Function"
category: "Core Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/ims-mgw/"
summary: "Mediální brána zajišťující konverzi mezi paketově přepínanými IMS mediálními proudy (např. přes RTP/IP) a formáty média s okruhovým přepínáním (např. TDM hlas). Umožňuje spolupráci mezi IMS sítěmi a s"
---

IMS-MGW je mediální brána, která provádí konverzi mezi paketově přepínanými IMS mediálními proudy a formáty s okruhovým přepínáním, aby umožnila spolupráci se staršími sítěmi pod řízením MGCF.

## Popis

Funkce IMS Media Gateway (IMS-MGW) je entita přenosové roviny odpovědná za spolupráci uživatelského média (např. hlasu, videa) mezi paketově přepínanou IP doménou IMS a staršími sítěmi s okruhovým přepínáním, jako je veřejná telefonní síť ([PSTN](/mobilnisite/slovnik/pstn/)) nebo starší GSM/UMTS jádrové sítě. Provádí skutečnou konverzi mediálních proudů mezi různými formáty a transportními protokoly. IMS-MGW je klíčovou součástí pro umožnění plynulých hlasových a multimediálních hovorů mezi účastníky IMS a uživateli v tradičních telefonních sítích.

Architektonicky je IMS-MGW řízena funkcí Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)), což je entita signalizační roviny, která zvládá konverzi protokolů mezi [SIP](/mobilnisite/slovnik/sip/) (používaným v IMS) a [ISUP](/mobilnisite/slovnik/isup/)/BICC (používanými v sítích s okruhovým přepínáním). MGCF řídí IMS-MGW pomocí protokolu H.248 (také známého jako [MEGACO](/mobilnisite/slovnik/megaco/)) podle definice referenčního bodu Mn v 3GPP. MGCF instruuje IMS-MGW k vytváření, modifikaci a mazání terminací a kontextů, které reprezentují logické mediální koncové body a spojení. Například MGCF může přikázat IMS-MGW, aby vytvořila spojení mezi IP terminací (přijímající [RTP](/mobilnisite/slovnik/rtp/) audio proud na konkrétní IP/port) a [TDM](/mobilnisite/slovnik/tdm/) terminací (na konkrétním časovém slotu E1).

Klíčová operace IMS-MGW zahrnuje zpracování média v reálném čase. Na straně IMS typicky zpracovává proudy Real-time Transport Protocol (RTP) a Real-time Transport Control Protocol ([RTCP](/mobilnisite/slovnik/rtcp/)) nesoucí zakódovaný hlas (např. pomocí kodeků AMR, G.711). Na straně s okruhovým přepínáním komunikuje s TDM (E1/T1) trasami nesoucími hlasové kanály s pulzně kódovou modulací (PCM) nebo s dalšími staršími rozhraními. Mezi její základní funkce patří transkódování média (konverze mezi různými hlasovými kodeky), transportní zpracování (paketizace/depaketizace, vyrovnávací paměť pro potlačení jitteru) a potlačení ozvěn. Může také podporovat detekci a generování tónů (např. pro DTMF tóny) a přehrávání oznámení.

V rámci sítě IMS se IMS-MGW neúčastní signalizace SIP; je čistě prostředkem mediální roviny pod příkazem MGCF. Toto oddělení řízení a média (podle modelu dekompozice brány) umožňuje škálovatelný, flexibilní a nákladově efektivní návrh sítě. MGCF a IMS-MGW mohou dodávat různí výrobci. IMS-MGW je nezbytná pro postupnou migraci ze sítí s okruhovým přepínáním na plně IP sítě, což operátorům umožňuje chránit investice do starších sítí a zároveň zavádět služby založené na IMS. Zajišťuje, že kvalita média a konektivita přenosové cesty jsou zachovány napříč technologickou hranicí.

## K čemu slouží

IMS-MGW byla vytvořena, aby vyřešila základní problém spolupráce média mezi novou, plně IP doménou IMS a rozsáhlou instalovanou základnou starších telefonních sítí s okruhovým přepínáním (PSTN, ISDN, GSM/UMTS CS jádro). Když byla IMS představena jako architektura pro poskytování multimediálních služeb přes IP, byla nutná migrační strategie. Nebylo proveditelné okamžitě nahradit veškerou stávající telefonní infrastrukturu a účastnická zařízení. Existovala kritická potřeba mostu, který by dokázal propojit IP hlasové/videohovory s tradičními telefonními linkami.

Účelem IMS-MGW je poskytnout tento most na úrovni přenosového nosiče média. Řeší nekompatibilitu mezi paketově přepínaným, RTP založeným transportem média v IMS a okruhově přepínaným, TDM založeným transportem ve starších sítích. Bez takové brány by byli účastníci IMS izolováni na "IP ostrově" a nemohli by komunikovat s většinou telefonních uživatelů po celém světě. IMS-MGW pod řízením MGCF provádí nezbytnou konverzi mediálních proudů v reálném čase, což umožňuje transparentní koncové hovory.

Její návrh následuje paradigma řídicího protokolu mediální brány (H.248/MEGACO), což byl v té době dobře etablovaný standard. To umožnilo znovupoužití stávající technologie a odborných znalostí mediálních bran, přičemž byla adaptována pro kontext 3GPP IMS. IMS-MGW umožňuje operátorům zavádět IMS postupně, zpočátku ji používat jako moderní nadstavbu pro trunking a propojení se staršími sítěmi. Řeší technickou výzvu udržení vysoké hlasové kvality a nízkého zpoždění při provádění složitých konverzí kodeků a transportu, což je zásadní pro přijetí nové síťové technologie zákazníky.

## Klíčové vlastnosti

- Transkódování média mezi IP kodeky (např. AMR) a kodeky pro okruhové přepínání (např. G.711 PCM)
- Transportní zpracování mezi nosiči RTP/UDP/IP a TDM (E1/T1)
- Řídicí rozhraní protokolu H.248 (MEGACO) (referenční bod Mn) s MGCF
- Potlačení ozvěn a vylepšení hlasové kvality
- Podpora detekce/generování tónů (DTMF) a oznámení
- Správa prostředků pro více souběžných mediálních spojení

## Definující specifikace

- **TS 28.705** (Rel-19) — IMS NRM IRP Information Service
- **TS 29.292** (Rel-19) — IMS Centralized Services (ICS) Interworking

---

📖 **Anglický originál a plná specifikace:** [IMS-MGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/ims-mgw/)
