---
slug: "ifc"
url: "/mobilnisite/slovnik/ifc/"
type: "slovnik"
title: "IFC – Initial Filter Criteria"
date: 2025-01-01
abbr: "IFC"
fullName: "Initial Filter Criteria"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ifc/"
summary: "Soubor spouštěcích bodů služby uložený v HSS a využívaný S-CSCF v IMS. Definuje podmínky, za kterých má být SIP zpráva pro uživatele předána konkrétním aplikačním serverům (AS) k vyvolání služeb."
---

IFC je soubor spouštěcích bodů služby uložený v HSS, který definuje podmínky, za kterých má S-CSCF předat SIP zprávu uživatele konkrétním aplikačním serverům.

## Popis

Počáteční filtrační kritéria (Initial Filter Criteria – iFC) jsou základní součástí mechanismu spouštění služeb v 3GPP IP Multimedia Subsystem (IMS). V podstatě se jedná o sadu pravidel či podmínek zřízených pro každého uživatele v jeho servisním profilu, který je uložen na Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Když se uživatel zaregistruje v IMS síti nebo zahájí/přijme SIP relaci (např. hovor), je jeho servisní profil včetně iFC stažen z HSS na přidělený Serving-Call Session Control Function (S-CSCF). S-CSCF je centrální signalizační uzel v IMS a funguje jako engine pro provádění služeb.

S-CSCF vyhodnocuje iFC pro každou počáteční SIP žádost (jako INVITE, REGISTER, SUBSCRIBE), která je spojena s daným uživatelem. Každé iFC obsahuje prioritu, spouštěcí bod a adresu aplikačního serveru ([AS](/mobilnisite/slovnik/as/)). Spouštěcí bod je logický výraz složený z Service Point Triggers (SPT). SPT je podmínka, která kontroluje konkrétní aspekty SIP zprávy, jako je Request-URI, SIP metoda, přítomnost nebo hodnota SIP hlavičky, informace v popisu relace (SDP) nebo stav registrace. Jsou-li podmínky ve spouštěcím bodu iFC splněny (vyhodnoceny jako ‚pravda‘), S-CSCF předá SIP žádost specifikovanému aplikačnímu serveru. AS pak poskytne vlastní službu, jako je kontinuita hlasového hovoru, přesměrování hovoru nebo multimediální telekomunikační aplikace.

S-CSCF zpracovává iFC podle pořadí priority. Když je žádost předána AS, může ji AS zpracovat a vrátit zpět S-CSCF k dalšímu zpracování. S-CSCF poté pokračuje v sekvenčním vyhodnocování zbývajících iFC, což umožňuje řetězení více služeb. Tento mechanismus poskytuje flexibilní, standardizovaný způsob, jak vyvolat širokou škálu služeb v určitém pořadí, aniž by byla servisní logika pevně zakódována v jádru S-CSCF, což umožňuje inovace služeb od operátorů i třetích stran.

## K čemu slouží

Účelem počátečních filtračních kritérií je umožnit flexibilní, na uživatele specifické spouštění služeb standardizovaným a odděleným způsobem v rámci IMS. Před IMS a iFC byly tradiční služby inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) pevně svázány s jádrem okruhového přepojování, používaly proprietární spouštěče a bylo obtížné je vytvářet a nasazovat. Mechanismus iFC to řeší vytvořením jasného oddělení mezi základní logikou řízení relace (ve S-CSCF) a aplikační/servisní logikou (v [AS](/mobilnisite/slovnik/as/)).

Tento návrh umožňuje síťovým operátorům a poskytovatelům třetích stran rychle vyvíjet a nasazovat nové multimediální služby bez nutnosti změn základních síťových prvků IMS. Řeší tak omezení monolitického softwaru ústředen, kde nové funkce vyžadovaly dlouhé a nákladné cykly upgradů. Spouštění založené na iFC je orientované na účastníka; různí uživatelé mohou mít aktivované různé sady služeb podle svého profilu. To byla klíčová motivace pro IMS: přejít od architektury služeb orientované na síť k architektuře orientované na uživatele, podporovat personalizované balíčky služeb a umožňovat funkce jako přenositelnost služeb mezi zařízeními a přístupovými sítěmi.

## Klíčové vlastnosti

- Ukládána v HSS jako součást IMS servisního profilu uživatele
- Vyhodnocována S-CSCF pro počáteční SIP žádosti
- Obsahují Service Point Triggers (SPT), které zkoumají komponenty SIP zprávy
- Směrují signalizaci SIP na konkrétní aplikační servery (AS) na základě podmínek
- Zpracovávána v definovaném pořadí priority, což umožňuje řetězení služeb
- Umožňují oddělení servisní logiky od základního řízení relace

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.407** (Rel-8) — OIP and OIR Simulation Services Protocol
- **TS 24.408** (Rel-7) — TIP/TIR Services Protocol Specification
- **TS 24.411** (Rel-8) — ACR and CB Service Protocol Specification
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.428** (Rel-7) — Common Basic Communication Procedures
- **TS 24.429** (Rel-7) — Explicit Communication Transfer (ECT) Service Specification
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.508** (Rel-8) — TIP and TIR Service Protocol Description
- **TS 24.524** (Rel-19) — Hosted Enterprise Services Architecture
- **TS 24.528** (Rel-8) — Common Basic Communication Procedures for IMS Services
- … a dalších 10 specifikací

---

📖 **Anglický originál a plná specifikace:** [IFC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ifc/)
