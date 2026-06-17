---
slug: "cfu"
url: "/mobilnisite/slovnik/cfu/"
type: "slovnik"
title: "CFU – Communication Forwarding Unconditional"
date: 2026-01-01
abbr: "CFU"
fullName: "Communication Forwarding Unconditional"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cfu/"
summary: "CFU je doplňková služba, která automaticky přesměruje všechny příchozí komunikační relace (hovory) na předem stanovené číslo bez vyzvánění na původní destinaci. Zajišťuje, aby uživatelé nikdy nezmeška"
---

CFU je doplňková služba, která automaticky přesměruje všechny příchozí hovory na předem stanovené číslo, aniž by nejprve zazvonila na původní destinaci.

## Popis

Communication Forwarding Unconditional (CFU, bezpodmínečné přesměrování komunikace) je základní doplňková služba v architektuře 3GPP, která poskytuje funkci automatického přesměrování hovorů. Služba funguje na síťové úrovni, zachytí příchozí komunikační relace dříve, než dorazí k zamýšlenému účastníkovu zařízení, a přesměruje je na předem nakonfigurovanou přesměrovací destinaci. K tomuto přesměrování dochází bezpodmínečně pro všechny příchozí relace, což znamená, že logika přesměrování nezávisí na stavu účastníka, jeho poloze ani na žádných jiných podmíněných faktorech.

Z architektonického hlediska je CFU implementována v rámci funkcí řízení služeb jádra sítě, konkrétně v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) pro okruhově spínané domény a v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) pro paketově spínané domény. Když dorazí komunikační relace do Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo do jádra IP Multimedia Subsystem (IMS), síť dotazuje profil služeb účastníka uložený v HLR/HSS. Pokud je CFU aktivní, síť načte přesměrovací číslo a relaci okamžitě přesměruje, aniž by se pokoušela navázat spojení s původní destinací. Proces přesměrování je pro volající stranu transparentní, která zažívá běžné procedury navazování hovoru.

Klíčové komponenty zapojené do implementace CFU zahrnují bod řízení služeb (HLR/HSS), bod přepínání služeb (MSC/IMS-CSCF) a databázi profilů služeb účastníka. Profil služeb obsahuje kritické parametry, jako je stav aktivace CFU, číslo přesměrovací destinace a platnost předplatného služby. Po aktivaci má CFU přednost před většinou ostatních doplňkových služeb, což zajišťuje konzistentní chování při přesměrování. Služba podporuje jak hlasové hovory, tak multimediální relace v prostředích IMS a zachovává kompatibilitu napříč různými generacemi sítí od 2G po 5G.

Fungování CFU zahrnuje několik protokolových interakcí mezi síťovými elementy. Když dorazí příchozí relace, MSC nebo IMS-CSCF odešle dotaz na HLR/HSS pomocí protokolů Mobile Application Part ([MAP](/mobilnisite/slovnik/map/)) nebo Diameter. HLR/HSS odpoví profilem služeb účastníka, včetně parametrů CFU, pokud je aktivní. Síť poté naváže relaci k přesměrovací destinaci pomocí standardních procedur navazování hovoru. Tento proces proběhne během milisekund, což zajišťuje minimální dopad na dobu navazování hovoru a zároveň poskytuje spolehlivou funkci přesměrování.

## K čemu slouží

CFU byla vytvořena k řešení základní potřeby spolehlivosti a dostupnosti komunikace v mobilních sítích. Před jejím zavedením účastníci, kteří nebyli dostupní, zmeškali důležité hovory, což vedlo k mezerám v komunikaci a potenciálním obchodním ztrátám. Služba tento problém řeší tím, že zajišťuje, aby veškerá příchozí komunikace dorazila k alternativní destinaci, kde ji účastník může přijmout, ať už jde o jiný telefon, linku v kanceláři nebo systém hlasové schránky.

Historicky se CFU objevila jako součást rámce doplňkových služeb GSM na počátku 90. let 20. století, navazujíc na podobné koncepty z pevné telefonie. Řešila omezení dřívějších mobilních systémů, kterým chyběly sofistikované schopnosti obsluhy hovorů. Bezpodmínečná povaha CFU poskytuje jednoduchost a spolehlivost ve srovnání s podmíněnými službami přesměrování, což ji činí vhodnou pro scénáře, kde účastníci potřebují konzistentní přesměrování bez ohledu na své okolnosti, například během dlouhodobé nepřítomnosti nebo při výhradním používání sekundárního zařízení.

Služba také podporuje efektivitu sítě snížením neúspěšných pokusů o spojení a zbytečných procedur pagingu. Když účastníci aktivují CFU, síť může okamžitě přesměrovat relace bez vynaložení prostředků na pokusy o lokalizaci nedostupných zařízení. Tato optimalizace je zvláště cenná v přetížených sítích nebo během špičkového vytížení. CFU navíc umožňuje různé obchodní aplikace, včetně nastavení virtuální kanceláře, směrování do call centra a služeb osobního čísla, které vyžadují spolehlivé možnosti přesměrování hovorů.

## Klíčové vlastnosti

- Bezpodmínečné přesměrování všech příchozích relací
- Implementace na síťové úrovni nevyžadující podporu zařízení
- Transparentní fungování pro volající strany
- Přednost před většinou ostatních doplňkových služeb
- Podpora jak okruhově spínaných, tak paketově spínaných domén
- Kompatibilita napříč sítěmi 2G, 3G, 4G a 5G

## Související pojmy

- [CFB – Call Forwarding on mobile subscriber Busy](/mobilnisite/slovnik/cfb/)
- [CFNRY – Call Forwarding on No Reply](/mobilnisite/slovnik/cfnry/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.273** (Rel-7) — IMS Multimedia Telephony with PSTN/ISDN Simulation
- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 24.173** (Rel-19) — Multimedia Telephony Service and Supplementary Services in IMS
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 24.404** (Rel-7) — Communication Diversion Services (CDIV)
- **TS 24.406** (Rel-8) — Message Waiting Indication (MWI) Protocol
- **TS 24.416** (Rel-7) — Malicious Call Identification Service
- **TS 24.447** (Rel-8) — Advice Of Charge (AOC) Service Protocol
- **TS 24.504** (Rel-8) — Communication Diversion Services Stage 3
- **TS 24.516** (Rel-8) — MCID Protocol Specification for NGN
- **TS 24.604** (Rel-19) — Communications Diversion (CDIV) Protocol Spec
- **TS 24.606** (Rel-19) — MWI Service Protocol Description
- … a dalších 8 specifikací

---

📖 **Anglický originál a plná specifikace:** [CFU na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfu/)
