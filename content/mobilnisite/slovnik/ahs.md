---
slug: "ahs"
url: "/mobilnisite/slovnik/ahs/"
type: "slovnik"
title: "AHS – Adaptive multirate Halfrate Speech"
date: 2025-01-01
abbr: "AHS"
fullName: "Adaptive multirate Halfrate Speech"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ahs/"
summary: "AHS je režim řečového kodeku, který dynamicky přepíná mezi polovičním a plným kanálovým kódováním za účelem optimalizace kapacity a kvality hovoru. Umožňuje efektivnější využití rádiových prostředků p"
---

AHS je režim řečového kodeku GSM, který dynamicky přepíná mezi polovičním (half-rate) a plným (full-rate) kanálovým kódováním, aby optimalizoval kapacitu a kvalitu hovoru přizpůsobením se síťovým podmínkám pro efektivnější využití rádiových prostředků.

## Popis

Adaptivní vícekanálový řečový kodek s poloviční rychlostí (Adaptive multirate Halfrate Speech, AHS) je sofistikovaný mechanismus řečového kódování a přenosu v GSM/[EDGE](/mobilnisite/slovnik/edge/) rádiové přístupové síti ([GERAN](/mobilnisite/slovnik/geran/)), který představuje vývoj základního adaptivního vícekanálového kodeku ([AMR](/mobilnisite/slovnik/amr/)). V jádru AHS funguje tak, že umožňuje síti dynamicky vybírat mezi režimy polovičného ([HR](/mobilnisite/slovnik/hr/)) a plného ([FR](/mobilnisite/slovnik/fr/)) hovorového kanálu ([TCH](/mobilnisite/slovnik/tch/)) pro hlasové hovory na základě aktuálních rádiových podmínek a vytížení sítě. Systém využívá rodinu kodeků AMR, která zahrnuje více režimů kodeku s různými přenosovými rychlostmi a úrovněmi ochrany proti chybám, ale přidává klíčovou schopnost adaptace režimu kanálu mezi přenosy typu [TCH/FS](/mobilnisite/slovnik/tch-fs-2/) (plný řečový kanál) a [TCH/HS](/mobilnisite/slovnik/tch-hs-2/) (poloviční řečový kanál).

Technická implementace zahrnuje průběžné sledování klíčových rádiových parametrů, jako je poměr nosná/interference (CIR), míra bitových chyb (BER) a míra ztráty rámců (FER), jak mobilní stanicí (MS), tak subsystémem základnové stanice (BSS). Na základě těchto měření a předem nastavených prahových hodnot nakonfigurovaných síťovými operátory může systém zahájit procedury adaptace režimu kanálu. Když to podmínky dovolí, může síť přepnout hovor z TCH/FS na TCH/HS, čímž efektivně zdvojnásobí hlasovou kapacitu na daném rádiovém kanálu tím, že umožní dvěma hovorům sdílet to, co bylo dříve alokováno pro jeden hovor. K této adaptaci dochází prostřednictvím ustavených signalizačních procedur definovaných ve specifikacích 3GPP, což zajišťuje minimální přerušení služby během přechodu.

Architektura podporující AHS zahrnuje vylepšení několika síťových prvků. BSS vyžaduje softwarové aktualizace k implementaci algoritmů adaptace režimu kanálu a signalizačních procedur. Mobilní stanice musí podporovat oba režimy kodeku AMR a schopnost přepínat mezi polovičními a plnými kanály. Jádrová síť, zejména Mobile Switching Center (MSC), musí podporovat nezbytnou signalizaci pro správu režimu kanálu. Systém funguje v rámci existující rámcové struktury GSM, přičemž TCH/HS využívá střídavé rámce mezi dvěma různými hovory na stejném časovém slotu, a zároveň zachovává zpětnou kompatibilitu se staršími zařízeními podporujícími AMR, která nepodporují funkci adaptivní poloviční rychlosti.

AHS hraje klíčovou roli v optimalizaci sítě tím, že poskytuje operátorům mocný nástroj pro správu kapacity. Během špičkového vytížení nebo v oblastech s omezenou kapacitou může síť automaticky převést více hovorů do režimu poloviční rychlosti, aby pojala další uživatele. Naopak, když se rádiové podmínky zhorší nebo během mimoprovozních hodin, se systém může vrátit do režimu plné rychlosti, aby poskytl vyšší kvalitu hovoru. K této dynamické adaptaci dochází bez nutnosti manuálního zásahu síťových operátorů, což z ní činí nezbytnou součást samooptimalizujících se sítí. Tato technologie představuje významný pokrok ve spektrální účinnosti hlasových služeb a prodlužuje užitečnou životnost sítí GSM, zatímco datové služby spotřebovávaly rostoucí podíl dostupného spektra.

## K čemu slouží

AHS byl vyvinut, aby řešil kritickou výzvu omezené dostupnosti spektra v sítích GSM při zachování přijatelné kvality hovoru. Jak počet mobilních účastníků exponenciálně rostl na konci 90. let a začátkem 21. století, čelili síťoví operátoři vážným kapacitním omezením, zejména v městských oblastech a během špičkového vytížení. Tradiční sítě GSM používaly pevné režimy kanálu – buď plnou, nebo poloviční rychlost – což představovalo kompromis mezi kapacitou a kvalitou. Plná rychlost poskytovala lepší kvalitu hovoru, ale obsloužila méně uživatelů, zatímco poloviční rychlost zdvojnásobila kapacitu na úkor snížené kvality hovoru, zejména ve špatných rádiových podmínkách.

Základním problémem, který AHS řešil, byl tento rigidní kompromis mezi kapacitou a kvalitou. Předchozí přístupy vyžadovaly manuální konfiguraci režimů kanálu nebo statické alokační politiky, které se nedokázaly přizpůsobit měnícím se síťovým podmínkám. Během vytížených hodin sítě nastavené na kvalitu zažívaly kongesce a blokované hovory, zatímco sítě nastavené na kapacitu trpěly špatnou kvalitou hovoru, i když bylo spektrum k dispozici pro lepší službu. AHS do tohoto rozhodovacího procesu vnesl inteligenci, což umožnilo sítím dynamicky se optimalizovat na základě skutečných podmínek namísto statických konfigurací.

Z historické perspektivy se AHS objevil jako součást širší standardizace kodeku AMR v 3GPP Release 4, přičemž specifické schopnosti adaptivní poloviční rychlosti byly definovány v následujících vydáních. Tento vývoj se časově shodoval s přechodem průmyslu k efektivnějšímu využití stávající infrastruktury, protože aukce spektra činily další frekvence neúměrně drahými. AHS umožnil operátorům odložit nákladná rozšíření sítě a zároveň zlepšit kvalitu služeb a kapacitu, čímž sloužil jako přechodová technologie mezi základními hlasovými službami GSM a paketovými hlasovými službami, které se později objevily se sítěmi 3G a 4G. Tato technologie řešila jak obchodní potřeby (snížení kapitálových výdajů), tak technické požadavky (zlepšení spektrální účinnosti) v jediném elegantním řešení.

## Klíčové vlastnosti

- Dynamická adaptace režimu kanálu mezi polovičnými a plnými řečovými kanály
- Integrace s rodinou kodeků AMR pro optimalizovanou kvalitu řeči při různých přenosových rychlostech
- Sledování rádiových podmínek v reálném čase včetně měření CIR, BER a FER
- Automatizovaná správa kapacity bez nutnosti manuální rekonfigurace sítě
- Zpětná kompatibilita se staršími mobilními stanicemi podporujícími AMR
- Podpora plynulých předávání mezi různými režimy kanálu během aktivních hovorů

## Definující specifikace

- **TS 26.247** (Rel-19) — 3GPP Progressive Download & DASH over HTTP
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TR 26.938** (Rel-19) — DASH Deployment Guidelines for 3GPP Networks
- **TR 45.914** (Rel-19) — MUROS Feasibility Study for Voice Capacity
- **TR 45.926** (Rel-19) — GERAN BTS Energy Saving Study

---

📖 **Anglický originál a plná specifikace:** [AHS na 3GPP Explorer](https://3gpp-explorer.com/glossary/ahs/)
