---
slug: "3pty"
url: "/mobilnisite/slovnik/3pty/"
type: "slovnik"
title: "3PTY – Three-Party Communication"
date: 2026-01-01
abbr: "3PTY"
fullName: "Three-Party Communication"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/3pty/"
summary: "3PTY umožňuje mobilnímu uživateli zřídit třístranný hovor přidáním třetí strany k existujícímu dvoustrannému hovoru, čímž vznikne vícesměrná komunikační relace. Tato služba je klíčová pro obchodní kon"
---

3PTY je služba, která umožňuje mobilnímu uživateli přidat třetí stranu do probíhajícího dvoustranného hovoru, čímž vytvoří třístrannou nebo vícesměrnou komunikační relaci.

## Popis

Komunikace tří stran (Three-Party Communication, 3PTY) je doplňková služba definovaná ve standardech 3GPP, která umožňuje obsluhovanému mobilnímu účastníkovi navázat komunikační relaci zahrnující tři strany. Služba funguje v rámci architektury IP Multimedia Subsystem (IMS) a využívá signalizaci Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) a protokoly pro řízení médií ke správě více současných spojení. Když uživatel zahájí relaci 3PTY, síť musí zvládnout složité signalizační toky, míchání médií a alokaci zdrojů, aby zajistila efektivní komunikaci všech stran.

Technická implementace zahrnuje koordinaci několika síťových prvků. Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) zpracovává SIP signalizaci pro požadavky 3PTY, zatímco Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) poskytuje schopnosti míchání médií pro kombinaci zvukových proudů od všech tří účastníků. User Equipment (UE) musí podporovat specifické SIP metody a hlavičky pro zahájení a správu relací 3PTY, včetně schopnosti stávající hovory přerušit (hold) během navazování nových spojení. Síť udržuje pro každého účastníka samostatný stav dialogu, přičemž navenek prezentuje jednotnou konferenci.

Mezi klíčové architektonické komponenty patří prvky jádra IMS, zejména MRF, která může být implementována jako samostatné Media Resource Function Controller ([MRFC](/mobilnisite/slovnik/mrfc/)) a Media Resource Function Processor ([MRFP](/mobilnisite/slovnik/mrfp/)) nebo jako kombinovaná Multimedia Resource Function (MRF). MRF zajišťuje operace v rovině médií, včetně míchání audia, transkódování mezi různými kodeky (je-li nutné) a správy Real-time Transport Protocol ([RTP](/mobilnisite/slovnik/rtp/)) proudů. S-CSCF koordinuje s MRF přes rozhraní Mr (pomocí SIP) k navázání a řízení mediálních relací.

Provoz služby následuje specifické procedury: nejprve obsluhovaný uživatel naváže dvoustranný hovor; za druhé tento hovor přeruší (hold) a naváže nové spojení s třetí stranou; za třetí uživatel aktivuje službu 3PTY, což vyvolá v síti připojení všech tří stran prostřednictvím MRF. Síť musí správně spravovat účtování, přičemž 3PTY je často považována za prémiovou službu se specifickými záznamy o účtování generovanými prostřednictvím Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) nebo Offline Charging System ([OFCS](/mobilnisite/slovnik/ofcs/)). Parametry Quality of Service (QoS) musí být zachovány pro všechny účastníky, což vyžaduje, aby Policy and Charging Rules Function (PCRF) alokovala odpovídající zdroje přenosových kanálů.

3PTY představuje základní vícesměrnou komunikační službu, která připravila cestu pro pokročilejší konferenční schopnosti v pozdějších vydáních 3GPP. Ačkoli byla ve své počáteční implementaci základní, stanovila důležité architektonické vzory pro míchání médií, správu relací a uživatelské ovládání, které ovlivnily následné služby multimediální telefonie. Služba demonstruje, jak se mobilní sítě vyvinuly z jednoduché komunikace bod-bod na podporu skupinových interakcí.

## K čemu slouží

3PTY byla vytvořena, aby uspokojila rostoucí potřebu základní vícesměrné komunikace v mobilních sítích, což umožnilo obchodním uživatelům, rodinám a sociálním skupinám vést třístranné rozhovory bez nutnosti specializovaných konferenčních můstků nebo externích služeb. Před standardizací 3PTY mobilní sítě primárně podporovaly pouze dvoustranné hovory, což uživatele nutilo používat řešení jako call waiting s ručním přepínáním nebo třetí stranou poskytované konferenční služby, které byly často nespolehlivé a drahé. Služba zaplnila důležitou mezeru v komunikačních schopnostech mobilních sítí, když se mobilní telefony staly všudypřítomnými pro osobní i profesionální použití.

Historický kontext vývoje 3PTY zahrnuje přechod od sítí s přepojováním okruhů k sítím s přepojováním paketů a vznik IMS jako platformy pro poskytování multimediálních komunikačních služeb. Ve vydání 8 se 3GPP snažilo definovat standardizovaný přístup k vícesměrným službám, který by konzistentně fungoval napříč různými síťovými operátory a výrobci zařízení. Předchozí proprietární implementace vytvářely problémy s interoperabilitou a omezovaly dostupnost služeb, zatímco standardizovaná služba 3PTY zajistila konzistentní uživatelský zážitek a širší přijetí na trhu.

3PTY vyřešila několik praktických problémů: odstranila nutnost, aby uživatelé ručně přepínali mezi hovory při koordinaci tří stran, poskytla standardizovaný model účtování pro vícesměrné hovory a zajistila konzistentní kvalitu zvuku pro všechny účastníky prostřednictvím síťově řízeného míchání médií. Služba také stanovila důležité precedenty pro to, jak sítě spravují více současných relací pro jednoho uživatele, což ovlivnilo pozdější vývoj pokročilejších konferenčních a kolaboračních služeb v rámci ekosystému 3GPP.

## Klíčové vlastnosti

- Umožňuje mobilnímu uživateli přidat třetí stranu k existujícímu dvoustrannému hovoru
- Využívá architekturu IMS s MRF pro míchání a řízení médií
- Podporuje signalizaci založenou na SIP pro navazování a správu relací
- Poskytuje konzistentní kvalitu zvuku prostřednictvím síťově řízeného zpracování médií
- Obsahuje standardizované mechanismy účtování pro vícesměrné relace
- Udržuje samostatné signalizační dialogy, přičemž prezentuje jednotný mediální zážitek

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MRF – Multimedia Resource Function](/mobilnisite/slovnik/mrf/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.827** (Rel-16) — Policy and Charging for Volume Based Charging
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony

---

📖 **Anglický originál a plná specifikace:** [3PTY na 3GPP Explorer](https://3gpp-explorer.com/glossary/3pty/)
