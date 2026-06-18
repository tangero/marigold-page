---
slug: "vmsc"
url: "/mobilnisite/slovnik/vmsc/"
type: "slovnik"
title: "VMSC – Visited Mobile Switching Center"
date: 2025-01-01
abbr: "VMSC"
fullName: "Visited Mobile Switching Center"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/vmsc/"
summary: "Ústředna mobilní sítě (MSC) v síti, ve které účastník právě roamuje. Zajišťuje pro navštívené účastníky řízení hovorů, spojování a správu mobility, což umožňuje plynulé roamování mezi různými síťovými"
---

VMSC (navštívená ústředna mobilní sítě) je ústředna mobilní sítě (MSC) v síti, ve které účastník právě roamuje, a zajišťuje pro tohoto navštíveného účastníka řízení hovorů, spojování a správu mobility.

## Popis

Visited Mobile Switching Center (VMSC, navštívená ústředna mobilní sítě) je prvek jádra sítě v okruhově spínaných ([CS](/mobilnisite/slovnik/cs/)) mobilních sítích, konkrétně v architekturách GSM, UMTS a raného LTE (pro CS fallback). Jedná se o [MSC](/mobilnisite/slovnik/msc/), která fyzicky obsluhuje mobilního účastníka nacházejícího se mimo geografickou oblast pokrytí jeho domovské sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)). Když účastník přejde do roamingu v cizí síti ([VPLMN](/mobilnisite/slovnik/vplmn/)), jeho zařízení se připojí k rádiové přístupové síti této navštívené sítě. MSC navštívené sítě, která tohoto účastníka obsluhuje, se pro danou relaci stává VMSC.

Z architektonického hlediska VMSC vykonává všechny standardní funkce MSC, ale pro navštíveného účastníka. Mezi její klíčové komponenty patří spínací pole pro propojení okruhově spínaných hlasových hovorů a Visitor Location Register ([VLR](/mobilnisite/slovnik/vlr/)), který je typicky umístěn společně s MSC. VLR je kritická databáze, která uchovává dočasnou kopii profilu služeb roamujícího účastníka, staženou z jeho Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) v domovské síti. Tento profil zahrnuje informace jako identita účastníka ([IMSI](/mobilnisite/slovnik/imsi/)), povolené služby a autentizační data. VMSC tyto informace využívá k poskytování služeb bez nutnosti dotazovat se na HLR při každé transakci, čímž se snižuje latence a signalizační zátěž na meziodvětvových spojích.

Role VMSC zahrnuje několik klíčových procedur. Při aktualizaci polohy VMSC/VLR zaregistruje přítomnost účastníka ve své servisní oblasti a informuje o tom HLR. Pro hovory iniciované mobilním zařízením ([MO](/mobilnisite/slovnik/mo/)) VMSC zřídí cestu hovoru. Pro hovory přijímané mobilním zařízením (MT) je hovor nejprve směrován do domovské sítě účastníka na GMSC (Gateway MSC). GMSC se dotáže HLR, aby zjistil aktuální polohu účastníka, a získá adresu VMSC. GMSC pak hovor přepošle na VMSC, která ve své rádiové síti provede paging, aby účastníka lokalizovala a dokončila zřízení hovoru. VMSC také zajišťuje předávání hovorů (handover) ve své vlastní oblasti a doplňkové služby pro navštíveného účastníka.

## K čemu slouží

VMSC existuje, aby umožnila plynulé národní a mezinárodní roamování, což je základní vlastnost mobilních sítí. Bez ní by mobilní telefon fungoval pouze v oblasti pokrytí sítě jeho domovského operátora. Tento koncept řeší problém poskytování nepřetržité služby účastníkům při jejich pohybu přes geografické hranice spravované různými síťovými operátory.

Historicky, před standardizovanými roamingovými dohodami a architekturami, byla mobilní telefonie omezena na lokální oblasti. Vývoj VMSC spolu s oddělením HLR/VLR a standardizovanými signalizačními protokoly, jako je MAP (Mobile Application Part), byl průlomem, který umožnil globální úspěch GSM. Vyřešil omezení služby v rámci jedné sítě vytvořením distribuovaného kooperativního systému, v němž si sítě mohly na základě komerčních dohod důvěryhodně obsluhovat zákazníky těch druhých.

Účelem VMSC je provádět řízení služeb a spojování v síti, kde se účastník fyzicky nachází, a přitom se spoléhat na domovskou síť (prostřednictvím HLR) v otázkách autorizace účastnických dat a hlavních záznamů o účtování. Toto rozdělení odpovědnosti umožňuje navštívené síti poskytovat rádiové a spínací prostředky, zatímco domovská síť si ponechává kontrolu nad profilem účastníka a účtováním. Tento model motivoval vytvoření standardizovaných rozhraní (např. rozhraní C/D mezi VLR a HLR) a bezpečnostních mechanismů pro zajištění důvěryhodné komunikace mezi operátory.

## Klíčové vlastnosti

- Řízení a spojování okruhově spínaných hovorů pro roamující účastníky
- Společné umístění s Visitor Location Register (VLR) pro dočasná účastnická data
- Rozhraní k Home Location Register (HLR) pro získání a aktualizaci profilu
- Provádění procedur správy mobility, jako je aktualizace polohy a předání hovoru (handover)
- Zřizování hovorů iniciovaných i přijímaných mobilním zařízením
- Podpora doplňkových služeb (např. přesměrování, zákaz hovorů) pro návštěvníky

## Související pojmy

- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [VLR – Visitor Location Register](/mobilnisite/slovnik/vlr/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 24.206** (Rel-7) — Voice Call Continuity Between CS and IMS
- **TS 32.240** (Rel-19) — Charging Management Architecture & Principles
- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.293** (Rel-19) — Proxy Function in Domestic Service Provider
- **TS 32.808** (Rel-8) — Common User Profile Storage Framework

---

📖 **Anglický originál a plná specifikace:** [VMSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/vmsc/)
