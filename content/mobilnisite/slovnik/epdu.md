---
slug: "epdu"
url: "/mobilnisite/slovnik/epdu/"
type: "slovnik"
title: "EPDU – External Protocol Data Unit"
date: 2025-01-01
abbr: "EPDU"
fullName: "External Protocol Data Unit"
category: "Protocol"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/epdu/"
summary: "External Protocol Data Unit (EPDU) je kontejner používaný v zapouzdření protokolové vrstvy, zejména v protokolu adaptace servisních dat (SDAP) v 5G NR a v LTE Positioning Protocol (LPP). Přenáší data"
---

EPDU je kontejner používaný v zapouzdření protokolové vrstvy, zejména v SDAP nebo LPP, který přenáší kompletní datovou jednotku protokolu vyšší vrstvy pro zpracování partnerskou entitou.

## Popis

External Protocol Data Unit (EPDU) je konceptuální datová struktura definovaná v rámci specifických specifikací protokolů 3GPP, která usnadňuje transparentní přenos protokolových dat mezi partnerskými entitami napříč vrstvovou architekturou. Není to samostatný protokol, ale definovaný kontejner nebo formát zapouzdření používaný jinými protokoly. EPDU typicky zapouzdřuje kompletní Protocol Data Unit (PDU) z vyšší vrstvy, včetně její hlavičky a užitečného zatížení, což umožňuje službě nižší vrstvy s ní zacházet jako s neprůhledným datovým blokem pro doručení. Tento mechanismus zajišťuje, že nižší vrstva nemusí interpretovat ani modifikovat vnitřní strukturu PDU vyšší vrstvy, čímž zachovává nezávislost protokolů a principy zapouzdření.

Jednou z primárních aplikací EPDU je použití v rámci Service Data Adaptation Protocol (SDAP) v uživatelské rovině 5G New Radio (NR), jak je specifikováno v 3GPP TS 38.415. V tomto kontextu vrstva SDAP přijímá QoS toky od core sítě. Pro každý QoS tok se Protocol Data Unit SDAP skládá z hlavičky SDAP a datové PDU SDAP. Datová PDU SDAP sama může nést EPDU, které obsahuje kompletní PDU z vyšší vrstvy (typicky IP vrstvy). Entita SDAP zpracovává EPDU na základě mapování QoS toků a reflexivních pravidel QoS, přidává nebo odstraňuje hlavičku SDAP podle potřeby, ale neupravuje obsah zapouzdřeného EPDU. To umožňuje efektivní mapování IP paketů na rádiové přenosy bez nutnosti, aby vrstva SDAP rozuměla sémantice IP hlaviček.

Dalším významným případem použití je v pozicovacích protokolech, jako je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) definovaný v TS 36.355. V LPP se EPDU používá k přenosu zpráv z jiných pozicovacích protokolů (např. LPPe - rozšíření LPP) uvnitř standardního kontejneru LPP zprávy. To umožňuje rozšiřitelnost a přenos dat specifických pro výrobce nebo dat budoucích pozicovacích protokolů zpětně kompatibilním způsobem. Vrstva LPP jednoduše zapouzdří celou PDU externího protokolu jako EPDU uvnitř LPP zprávy a přepošle ji partnerovi. Vrstva LPP partnerské entity extrahuje EPDU a doručí jej příslušné entitě externího protokolu ke zpracování. Tento návrhový vzor podporuje modularitu a umožňuje různým protokolovým zásobníkům vzájemně spolupracovat bez těsného provázání.

## K čemu slouží

Koncept External Protocol Data Unit (EPDU) byl standardizován, aby řešil potřebu čistého oddělení a transparentního tunelování mezi protokolovými vrstvami nebo mezi různými sadami protokolů. Ve složitých telekomunikačních systémech je často nutné, aby jeden protokol přenášel data generovaná jiným, potenciálně nesouvisejícím protokolem, aniž by přenášející protokol musel rozumět vnitřnímu formátu nebo sémantice přenášených dat. Před takovou formalizací mohly ad-hoc metody zapouzdření vést k problémům s interoperabilitou, snížené flexibilitě a zvýšené složitosti při zavádění nových protokolů nebo rozšíření.

V kontextu 5G SDAP byl mechanismus EPDU klíčový pro návrh flexibilní uživatelské roviny, která podporuje rozmanité služby s různými požadavky na QoS. SDAP potřeboval mapovat IP toky na rádiové přenosy na základě pravidel QoS, ale zacházení s IP pakety jako s neprůhlednými EPDU znamenalo, že návrh vrstvy SDAP mohl být zjednodušen a připraven na budoucnost. Mohla by zpracovávat jakýkoli formát PDU vyšší vrstvy (IPv4, IPv6, Ethernet nebo budoucí protokoly) beze změny, pokud byl prezentován jako EPDU. To podporuje vizi 5G jako službami řízené architektury schopné podporovat širokou škálu vertikálních odvětví.

Pro pozicovací protokoly jako [LPP](/mobilnisite/slovnik/lpp/) slouží EPDU jako prostředek umožňující rozšiřitelnost. Pozicovací technologie se rychle vyvíjejí a vznikají nové metody a vylepšení. Definováním standardního kontejneru (EPDU) pro data externích pozicovacích protokolů může LPP přenášet zprávy pro nové, nepředvídané protokoly bez nutnosti změn základní specifikace LPP. To umožňuje výrobcům zařízení a sítí inovovat a přidávat proprietární nebo standardizovaná rozšíření (jako LPPe) strukturovaným, interoperabilním způsobem, což zajišťuje stabilitu základních implementací LPP při současné podpoře nových funkcí.

## Klíčové vlastnosti

- Slouží jako kontejner pro kompletní Protocol Data Unit (PDU) vyšší vrstvy (hlavičku i užitečné zatížení)
- Umožňuje transparentní tunelování mezi protokolovými vrstvami bez sémantické interpretace
- Používá se v 5G SDAP pro mapování QoS toků obsahujících IP pakety na rádiové přenosy
- Využívá se v LPP pro přenos zpráv z externích pozicovacích protokolů
- Podporuje nezávislost protokolů a modularitu v návrhu systému
- Usnadňuje zpětně kompatibilní rozšiřitelnost pro budoucí protokoly

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)

## Definující specifikace

- **TS 36.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 37.355** (Rel-19) — LTE Positioning Protocol (LPP)
- **TS 38.415** (Rel-19) — PDU Session User Plane Protocol

---

📖 **Anglický originál a plná specifikace:** [EPDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/epdu/)
