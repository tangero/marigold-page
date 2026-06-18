---
slug: "esqk"
url: "/mobilnisite/slovnik/esqk/"
type: "slovnik"
title: "ESQK – Emergency Service Query Key"
date: 2025-01-01
abbr: "ESQK"
fullName: "Emergency Service Query Key"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/esqk/"
summary: "Dočasný identifikátor používaný ke korelaci nouzového hovoru s lokalizačními a údaji o účastníkovi v IP multimediální podsystému (IMS). Je klíčový pro směrování nouzových hovorů na správné středisko t"
---

ESQK je dočasný identifikátor používaný v IMS ke korelaci nouzového hovoru s lokalizačními a údaji o účastníkovi za účelem směrování na správné PSAP a poskytnutí přesných informací o volajícím.

## Popis

Emergency Service Query Key (ESQK) je klíčový prvek v architektuře nouzových služeb 3GPP IMS, definovaný primárně v TS 23.167. Funguje jako dočasný, jedinečný klíč přidělený sítí na dobu trvání nouzové relace. Když uživatel iniciuje nouzový hovor přes síť IMS, je hovor směrován na funkci Emergency Call Session Control Function ([E-CSCF](/mobilnisite/slovnik/e-cscf/)). E-CSCF ve spolupráci s funkcí Location Retrieval Function ([LRF](/mobilnisite/slovnik/lrf/)) zodpovídá za získání polohy volajícího. ESQK je vygenerován a asociován s touto konkrétní nouzovou relací a s odpovídajícími lokalizačními údaji.

ESQK je následně vložen do signalizace protokolu Session Initiation Protocol ([SIP](/mobilnisite/slovnik/sip/)) nouzového hovoru, typicky v Request-URI nebo v dedikované hlavičce. Když je hovor směrován na středisko tísňového volání ([PSAP](/mobilnisite/slovnik/psap/)), systém PSAP použije přijatý ESQK jako dotazovací klíč. PSAP odešle tento ESQK v dotazu na určenou entitu sítě nouzových služeb, jako je Emergency Services Message Entity (ESME) nebo přes framework protokolu LoST (Location-to-Service Translation), aby získal asociované lokalizační informace a další data o hovoru z databáze sítě, kam je uložil E-CSCF/LRF.

Tento mechanismus odděluje cestu hlasového hovoru v reálném čase od cesty pro získávání lokalizačních dat, což je zásadní pro efektivitu a spolehlivost. PSAP nemusí parsovat komplexní lokalizační objekty uvnitř samotné SIP signalizace; jednoduše použije odlehčený ESQK k načtení dat. Tato architektura podporuje jak počáteční získání polohy, tak následné aktualizace polohy, protože síť může poslat aktualizované lokalizační informace do stejného záznamu v databázi klíčovaného pomocí ESQK. ESQK je dočasný a platný pouze po dobu životnosti nouzové relace, po jejímž skončení může být recyklován, což zajišťuje soukromí a efektivní využití zdrojů.

Klíčové komponenty spojené s ESQK zahrnují uživatelské zařízení (UE), Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), který detekuje nouzový požadavek, E-CSCF, který spravuje nouzovou relaci, LRF, který získává a formátuje lokalizační informace, a infrastrukturu PSAP. ESQK umožňuje standardizované, interoperabilní rozhraní mezi IMS jádrem mobilního operátora a různorodými systémy PSAP, které mohou být provozovány různými autoritami. Jeho role je základní pro služby Next Generation emergency services (NG-eCall, IMS nouzové hovory), kde je přesná, ze sítě odvozená poloha prvořadá.

## K čemu slouží

ESQK byl zaveden k řešení kritických problémů při směrování nouzových hovorů a doručování lokalizačních informací v IP sítích, konkrétně v IMS. Tradiční nouzové hovory v komutovaných sítích často vkládaly lokalizační data přímo do signalizace hovoru nebo spoléhaly na identifikátor buňky dostupný [PSAP](/mobilnisite/slovnik/psap/), což mohlo být nepřesné nebo nedostatečné pro rychlý zásah, zvláště u mobilních uživatelů. Jak se sítě vyvíjely k architekturám plně v IP, byla potřeba nová, standardizovaná metoda ke korelaci hlasového hovoru s dynamicky získanými, přesnými lokalizačními daty.

Primární motivací bylo oddělit doručení hlasového média nouzového hovoru od doručení asociovaných dat (jako jsou [GPS](/mobilnisite/slovnik/gps/) souřadnice nebo adresa). Toto oddělení umožňuje každému systému – síti pro směrování hlasu a systému databáze poloh – pracovat optimálně. Také zohledňuje skutečnost, že PSAP může potřebovat dotazovat se na polohu až po přijetí hovoru a může vyžadovat aktualizované polohy, pokud se volající pohybuje. ESQK poskytuje jednoduchý, univerzální 'klíč', který propojuje tyto dva světy, a umožňuje PSAP od různých dodavatelů a regionů interoperabilitu se sítěmi kompatibilními s 3GPP bez nutnosti hluboké integrace do interních lokalizačních systémů operátora.

Dále řeší obavy o soukromí a bezpečnost použitím dočasného, neosobního identifikátoru. ESQK neprozrazuje PSAP telefonní číslo volajícího ([MSISDN](/mobilnisite/slovnik/msisdn/)) ani trvalý identifikátor účastníka, dokud nejsou explicitně načteny, pokud to politika umožňuje. Tato architektura, založená na ESQK, byla základním krokem k spolehlivým, lokalizaci podporujícím nouzovým službám v LTE a 5G, podporujícím regulatorní požadavky jako E911 v USA a eCall v Evropě.

## Klíčové vlastnosti

- Dočasný identifikátor relace jedinečně přidělený na každý nouzový hovor v IMS
- Koreluje nouzovou hlasovou relaci s asociovanými lokalizačními daty v síťové databázi
- Vložen do SIP signalizace (např. v Request-URI) pro směrování a identifikaci
- Použit PSAP jako dotazovací klíč k získání polohy volajícího a dat ze sítě
- Umožňuje oddělenou architekturu, která odděluje hlasovou cestu od cesty pro získávání lokalizačních dat
- Podporuje soukromí tím, že se vyhýbá přímému přenosu osobních identifikátorů v počáteční signalizaci

## Související pojmy

- [E-CSCF – Emergency – Call Session Control Function](/mobilnisite/slovnik/e-cscf/)
- [PSAP – Public Safety Answering Point](/mobilnisite/slovnik/psap/)
- [ESRK – Emergency Service Routing Key](/mobilnisite/slovnik/esrk/)

## Definující specifikace

- **TS 23.167** (Rel-19) — IMS Emergency Sessions

---

📖 **Anglický originál a plná specifikace:** [ESQK na 3GPP Explorer](https://3gpp-explorer.com/glossary/esqk/)
