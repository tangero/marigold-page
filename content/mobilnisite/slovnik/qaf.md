---
slug: "qaf"
url: "/mobilnisite/slovnik/qaf/"
type: "slovnik"
title: "QAF – Q-Adapter Function"
date: 2025-01-01
abbr: "QAF"
fullName: "Q-Adapter Function"
category: "Management"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/qaf/"
summary: "Q-Adapter Function (QAF) je funkce síťového managementu (TMN) dle 3GPP, která poskytuje zprostředkování mezi spravovanou entitou nekompatibilní s TMN (např. zařízení používající SNMP) a operačním syst"
---

QAF je funkce síťového managementu (TMN) dle 3GPP, která zprostředkovává komunikaci mezi spravovanou entitou nekompatibilní s TMN a operačním systémem (OS) kompatibilním s TMN prostřednictvím adaptace protokolů a informačních modelů.

## Popis

Q-Adapter Function (QAF) je formalizovaná logická funkce v architektuře Telekomunikačního managementového systému ([TMN](/mobilnisite/slovnik/tmn/)) dle 3GPP, podrobně popsaná ve specifikaci 21.905. Zaujímá specifickou pozici v logické architektuře bloků TMN, kde funguje jako prostředník mezi světem managementu TMN a spravovaným světem nekompatibilním s TMN. Přestože je podobná obecnému konceptu Q Interface Adapter ([QA](/mobilnisite/slovnik/qa/)), QAF je obvykle specifikována s přesnějšími požadavky na chování a informační modelování. Jejím primárním úkolem je poskytnout kompletní adaptační vrstvu, díky které se jeden či více síťových prvků ([NE](/mobilnisite/slovnik/ne/)) nebo dokonce celé podsítě nekompatibilní s TMN jeví nadřazenému operačnímu systému (OS) či řídicímu systému jako jediná, logická entita kompatibilní s TMN.

Z provozního hlediska QAF na své severní straně plní úplnou roli agenta TMN, komunikuje s OS přes standardizované rozhraní Q (Qx nebo Q3). Používá standardní protokoly TMN jako [CMIP](/mobilnisite/slovnik/cmip/) a pracuje s definovanou bází managementových informací ([MIB](/mobilnisite/slovnik/mib/)) spravovaných objektů ([MO](/mobilnisite/slovnik/mo/)), které reprezentují adaptované prostředky. Na své jižní straně komunikuje se skutečnými prostředky nekompatibilními s TMN pomocí jejich nativních managementových protokolů, jako jsou [SNMP](/mobilnisite/slovnik/snmp/), TL1, [CORBA](/mobilnisite/slovnik/corba/) nebo proprietární rozhraní. QAF je zodpovědná za kompletní správu životního cyklu proxy spravovaných objektů, které vytváří. To zahrnuje vytváření instancí MO odpovídajících fyzickým nebo logickým prostředkům v adaptované síti, udržování jejich atributů pomocí dotazování (polling) nebo odběru událostí ze skutečných zařízení, mapování a předávání příkazů z OS na zařízení a překlad událostí/výstrah ze zařízení do standardních notifikací TMN.

Z architektonického hlediska obsahuje QAF klíčové komponenty: mediační modul pro konverzi protokolů a dat, správce instancí MO, který udržuje strom proxy objektů, a často lokální databázi pro ukládání stavových informací do mezipaměti. Nefunguje pouze jako prostý průchod protokolem; aktivně koreluje informace, může agregovat data z více zařízení do sumárních MO a může implementovat managementovou logiku, například upozornění na překročení prahových hodnot. Vytvořením této virtuální TMN vrstvy QAF umožňuje OS kompatibilnímu s TMN provádět plnohodnotný FCAPS management (správu chyb, konfigurace, účtování, výkonu a zabezpečení) na jinak nekompatibilním zařízení, což je zásadní pro správu hybridních sítí.

## K čemu slouží

Q-Adapter Function byla vyvinuta za účelem rozšíření výhod standardizovaného rámce TMN na širší ekosystém síťového vybavení, které nebylo navrženo s ohledem na TMN. Když se TMN stala cílovou architekturou pro management sítí 3GPP, významnou výzvou byla existence velkého množství před-TMN zařízení (např. IP směrovače, Ethernetové přepínače, starší přenosová technika) a zařízení z domén, kde dominovaly jiné standardy (jako IETF/SNMP). Prostá výměna tohoto vybavení nebyla možná.

QAF poskytuje strategickou cestu migrace a integrační řešení. Řeší omezení čistě nativního světa TMN definováním formalizované funkce, jejímž jediným úkolem je být 'mostem'. To umožňuje síťovým operátorům vytvářet jednotné systémy pro podporu provozu (OSS) založené na TMN pro správu služeb end-to-end, a to i tehdy, když podkladové síťové segmenty používají různé technologie. QAF řeší problém sil managementu. Bez ní by operátor potřeboval samostatné OSS pro síťové prvky 3GPP spravované přes TMN a další pro IP infrastrukturu spravovanou přes SNMP, což by bránilo zajištění služeb (service assurance) a korelaci chyb.

Navíc formalizace QAF, na rozdíl od obecného adaptérového konceptu, zajistila konzistenci v tom, jak jsou prostředky nekompatibilní s TMN modelovány a zpřístupňovány. To umožnilo vývoj znovupoužitelných implementací QAF pro běžné adaptační scénáře (např. SNMP na CMIP), což snižuje integrační náklady. Jejím účelem je v zásadě integrace, standardizace a ochrana stávajících investic, což umožňuje kohezní pohled managementu klíčový pro provoz složitých telekomunikačních sítí s více technologiemi.

## Klíčové vlastnosti

- Formálně definovaná logická funkce v architektuře TMN dle 3GPP pro zprostředkování mezi systémy TMN a systémy nekompatibilními s TMN.
- Plní úplnou roli agenta TMN, prezentuje proxy spravované objekty (MO) severnímu operačnímu systému (OS).
- Překládá mezi protokoly TMN (např. CMIP) a protokoly nekompatibilními s TMN (např. SNMP, TL1, CORBA).
- Mapuje informační modely nekompatibilní s TMN do standardizované báze managementových informací (MIB) TMN.
- Spravuje životní cyklus proxy MO, včetně jejich vytváření, aktualizace a mazání na základě stavu adaptovaných prostředků.
- Umožňuje FCAPS management staršího a ne-3GPP vybavení prostřednictvím jednotného rozhraní kompatibilního s TMN.

## Související pojmy

- [TMN – Telecommunications Management Network](/mobilnisite/slovnik/tmn/)
- [SNMP – Simple Network Management Protocol](/mobilnisite/slovnik/snmp/)
- [CMIP – Common Management Information Protocol](/mobilnisite/slovnik/cmip/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [QAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/qaf/)
