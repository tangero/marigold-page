---
slug: "r-sgw"
url: "/mobilnisite/slovnik/r-sgw/"
type: "slovnik"
title: "R-SGW – Roaming Signalling Gateway"
date: 2025-01-01
abbr: "R-SGW"
fullName: "Roaming Signalling Gateway"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/r-sgw/"
summary: "Síťová funkce v subsystému IP multimédií (IMS), která slouží jako signalizační brána pro roamující účastníky. Usnadňuje propojení mezi sítěmi různých operátorů prováděním překladu protokolů, typicky m"
---

R-SGW je síťová funkce v IMS, která slouží jako signalizační brána pro roamující účastníky a propojuje sítě operátorů prostřednictvím překladu protokolů, aby umožnila služby IMS.

## Popis

Roaming Signalling Gateway (R-SGW) je základní síťový prvek v architektuře subsystému IP multimédií (IMS) podle 3GPP, definovaný pro zpracování signalizačního propojení v roamovacích scénářích. Jeho hlavní rolí je sloužit jako signalizační bod propojení mezi navštívenou sítí (kde se účastník nachází v roamingu) a domovskou sítí (kde jsou uloženy profil a služby účastníka). R-SGW pracuje na referenčním bodu Mm, což je rozhraní mezi sítí IMS a jinou IP multimediální sítí, často IMS jiného operátora nebo sítí s přepojováním okruhů.

Funkčně je R-SGW zodpovědný za nezbytnou adaptaci protokolů a přenos zpráv. V raných nasazeních IMS a při propojování se staršími sítěmi to často zahrnuje překlad mezi zprávami protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) používanými v jádru IMS a protokoly založenými na signalizačním systému č. 7 ([SS7](/mobilnisite/slovnik/ss7/)), jako je [ISDN](/mobilnisite/slovnik/isdn/) User Part ([ISUP](/mobilnisite/slovnik/isup/)) nebo Bearer Independent Call Control (BICC), používanými v tradičních sítích s přepojováním okruhů. Tento překlad provádí na signalizační úrovni pro řízení relace, čímž zajišťuje, že zprávy pro sestavení, změnu a ukončení hovoru jsou správně pochopeny přes hranice sítí. R-SGW nezpracovává přenos uživatelských dat (hlas nebo média); jde čistě o signalizační bránu.

Architektonicky je R-SGW součástí funkcí hraniční kontroly v IMS. Spolupracuje s dalšími hraničními prvky, jako je Interconnection Border Control Function ([IBCF](/mobilnisite/slovnik/ibcf/)) a Transition Gateway (TrGW). Zatímco IBCF poskytuje celkové řízení relace na hranici, R-SGW poskytuje specifickou funkci propojení pro signalizační protokoly. Pro roamujícího účastníka zahajujícího hovor může signalizace proudit z jeho uživatelského zařízení (UE) přes Call Session Control Function ([CSCF](/mobilnisite/slovnik/cscf/)) navštívené sítě k R-SGW na hranici domovské sítě. R-SGW zajišťuje správné formátování a směrování signalizace do [S-CSCF](/mobilnisite/slovnik/s-cscf/) domovské sítě nebo k cílové síti, ať už jde o jinou IMS síť nebo starší síť s přepojováním okruhů. To umožňuje plynulou kontinuitu služeb a roaming pro služby založené na IMS, jako je Voice over LTE (VoLTE).

## K čemu slouží

R-SGW byl vytvořen, aby vyřešil kritický problém signalizační interoperability mezi novými, plně IP sítěmi IMS a stávajícím, rozšířeným světem telefonie s přepojováním okruhů, zejména v roamovacích scénářích. Když 3GPP definovalo IMS ve verzi 5 jako platformu pro poskytování multimediálních služeb, byla potřeba migrační cesta. Operátoři nemohli okamžitě nahradit veškerou starší infrastrukturu. Účastníci roamující v sítích s odlišnými technologickými profily potřebovali plynule uskutečňovat a přijímat hovory.

Bez brány jako je R-SGW by účastník IMS roamující v oblasti obsluhované pouze starší sítí s přepojováním okruhů nemohl sestavit hovory, protože signalizační protokoly ([SIP](/mobilnisite/slovnik/sip/) vs. ISUP/SS7) by byly nekompatibilní. R-SGW poskytuje nezbytnou překladovou vrstvu. Umožňuje domovské síti IMS řídit služby pro svého roamujícího účastníka, i když navštívená síť používá jinou podkladovou signalizační technologii. To bylo klíčové pro počáteční zavádění a adopci služeb založených na IMS, jako je VoLTE, a zajištění jejich globální funkčnosti napříč heterogenní síťovou infrastrukturou.

Historicky byla signalizace pro roaming zpracovávána bránami SS7 v jádru s přepojováním okruhů. R-SGW rozšiřuje tento koncept do éry IMS. Řeší omezení čistě SIPové sítě, která by byla izolovaná od rozsáhlé instalované základny sítí s přepojováním okruhů. Provedením propojení protokolů R-SGW umožnil postupný přechod k plně IP sítím, ochránil stávající investice a zajistil univerzální dostupnost služeb pro první uživatele IMS/VoLTE, což byl základní obchodní požadavek operátorů.

## Klíčové vlastnosti

- Poskytuje signalizační propojení mezi sítěmi IMS/SIP a staršími sítěmi založenými na SS7 (např. ISUP, BICC)
- Umístěn na referenčním bodu Mm pro propojení mezi IP multimediálními sítěmi
- Zpracovává překlad protokolů pouze pro signalizaci řízení relace, nikoli pro přenos uživatelských dat
- Umožňuje kontinuitu služeb IMS pro účastníky roamující v oblastech se staršími sítěmi
- Funguje jako součást architektury hraniční kontroly IMS, často spolu s IBCF
- Usnadňuje signalizaci pro sestavení, změnu a uvolnění hovoru přes hranice síťových technologií

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [IBCF – Interconnection Border Control Functions](/mobilnisite/slovnik/ibcf/)
- [CSCF – Call Session Control Function](/mobilnisite/slovnik/cscf/)
- [SS7 – Signalling System Number 7](/mobilnisite/slovnik/ss7/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [R-SGW na 3GPP Explorer](https://3gpp-explorer.com/glossary/r-sgw/)
