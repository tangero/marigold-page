---
slug: "lsbf"
url: "/mobilnisite/slovnik/lsbf/"
type: "slovnik"
title: "LSBF – Location System Billing Function"
date: 2025-01-01
abbr: "LSBF"
fullName: "Location System Billing Function"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lsbf/"
summary: "Location System Billing Function (LSBF) je síťový prvek zodpovědný za generování účtovacích záznamů pro služby založené na poloze. Má rozhraní k Location System Control Function (LSCF) a k účtovacímu"
---

LSBF je síťový prvek zodpovědný za generování účtovacích záznamů pro služby založené na poloze prostřednictvím rozhraní s řídicí funkcí lokalizačního systému a s jádrovým účtovacím systémem.

## Popis

Location System Billing Function (LSBF) je specializovaná logická funkce v architektuře 3GPP pro lokalizační služby ([LCS](/mobilnisite/slovnik/lcs/)). Funguje jako součást účtovací domény sítě, konkrétně uzpůsobená pro zpracování specifických požadavků na účtování spojených se zjišťováním a hlášením geografické polohy mobilního účastníka. LSBF není nutně samostatný fyzický uzel; její funkčnost může být integrována do stávajících účtovacích systémů nebo vyhrazených servisních platforem. Jejím klíčovým úkolem je shromažďovat účtovací data související s žádostmi o polohu, zpracovat tato data do příslušných účtovacích záznamů a předat tyto záznamy účtovacímu systému sítě pro fakturaci účastníkovi nebo pro vypořádání mezi operátory.

Z architektonického hlediska má LSBF rozhraní k Location System Control Function ([LSCF](/mobilnisite/slovnik/lscf/)), což je centrální koordinační entita pro žádosti o polohu. Když je vyvolána lokalizační služba – ať už samotným účastníkem (Mobile Originated Location Request), externím klientem (Mobile Terminated Location Request) nebo sítí pro tísňové volání – LSCF spravuje proces určování polohy. Po úspěšném dokončení (nebo selhání) pokusu o lokalizaci LSCF vygeneruje záznam o účtovacích datech ([CDR](/mobilnisite/slovnik/cdr/)) nebo podobnou hlášenou událost obsahující podrobnosti, jako je žádající klient, cílový účastník, typ služby (např. tísňová, komerční), dosažená přesnost, použitá metoda určení polohy a časová razítka. Tato účtovací data jsou následně přenesena do LSBF.

LSBF zpracovává tyto nezpracované účtovací události. Mezi její klíčové vnitřní komponenty patří moduly pro sběr účtovacích dat, korelaci událostí, aplikaci tarifů a formátování záznamů. Aplikuje příslušné tarifní politiky na základě typu služby, profilu účastníka a pravidel síťového operátora. Například žádost o polohu pro tísňovou službu může být účtována nulovou sazbou nebo může generovat záznam pro proplacení vládou, zatímco komerční žádost o vysokou přesnost pro navigační službu bude zpoplatněna. LSBF naformátuje konečný účtovací záznam, typicky standardizovaný CDR, a přenese jej do centrálního účtovacího systému sítě nebo účetní funkce. Toto oddělení umožňuje, aby se architektura LCS mohla soustředit na technologii určování polohy, zatímco složitá komerční a regulační účtovací logika je delegována na vyhrazenou účtovací doménu.

Její role v síti je klíčová pro komerční životaschopnost a regulatorní shodu lokalizačních služeb. Přesným zachycením a oceněním lokalizačních událostí umožňuje LSBF operátorům nabízet placené LCS podnikům a spotřebitelům. Zajišťuje také, že služby vyžadované zákonem, jako je lokalizace volajících během tísňových scénářů (E911/eCall), mohou být vhodně účtovány příslušným úřadům nebo pohlceny jako náklad služby. Dále, v roamingu může LSBF (v navštívené síti) generovat účtovací záznamy pro vypořádání s domovskou sítí účastníka, což usnadňuje účtování mezi operátory za lokalizační služby využívané v zahraničí.

## K čemu slouží

LSBF byla vytvořena, aby řešila specifické výzvy účtování spojené se službami založenými na poloze v mobilních sítích. Tradiční hlasové a datové služby mají relativně přímočaré účtovací modely založené na délce trvání, objemu nebo události. Lokalizační služby však zavádějí nové dimenze pro účtování: typ žádosti (tísňová, přidaná hodnota), požadovaná přesnost, doba odezvy a použité podkladové technologie určování polohy (např. Cell-ID, [OTDOA](/mobilnisite/slovnik/otdoa/), [A-GPS](/mobilnisite/slovnik/a-gps/)). LSBF existuje proto, aby převedla tyto technické parametry služby na účtovatelné události, čímž řeší problém, jak zpeněžit a evidovat síťové zdroje spotřebované při určování polohy účastníka.

Historicky vznikly lokalizační služby z regulatorních požadavků na lokalizaci tísňových volajících (E911 v USA, E112 v Evropě). Tato nařízení vyžadovala, aby sítě poskytovaly informace o poloze tísňovým službám, ale související náklady bylo třeba sledovat a potenciálně proplácet. LSBF pro to poskytla standardizovaný mechanismus. Následně, s nástupem komerčních [LCS](/mobilnisite/slovnik/lcs/) pro navigaci, sledování vozového parku a lokalizační reklamu, se flexibilní a robustní účtovací funkce stala nezbytnou pro obchodní modely. Před jejím definováním operátoři postrádali standardizovaný způsob účtování těchto služeb, což vedlo k proprietárním a neinteroperabilním řešením.

Motivace pro LSBF byla hnací silou potřeby jasného oddělení kompetencí v rámci architektury LCS. Funkce řízení určování polohy ([LSCF](/mobilnisite/slovnik/lscf/)) a provádění (např. [SAS](/mobilnisite/slovnik/sas/), SMLC) jsou složité a specifické pro technologii. Přenesením veškeré účtovací logiky na vyhrazenou LSBF se celý systém stává modulárnějším a škálovatelnějším. Toto oddělení umožňuje nezávisle aktualizovat účtovací pravidla a tarify bez ohledu na technologii určování polohy a umožňuje konzistentní účtování napříč různými přístupovými sítěmi (GERAN, UTRAN, E-UTRAN). Řeší tak omezení dřívějších ad-hoc přístupů, kde byla účtovací data vedlejším produktem, což mohlo vést k úniku výnosů nebo neschopnosti splnit regulatorní požadavky na účtování tísňových služeb.

## Klíčové vlastnosti

- Generuje a zpracovává záznamy o účtovacích datech (CDR) specificky pro události lokalizačních služeb.
- Má rozhraní k Location System Control Function (LSCF) pro přijímání účtovacích spouštěčů a hlášení událostí.
- Aplikuje tarifní politiky na základě typu služby (tísňová, komerční), přesnosti a profilu účastníka.
- Formátuje účtovací záznamy pro přenos do centrálního účtovacího systému sítě nebo účetní funkce.
- Podporuje účtování jak pro mobilní odchozí, tak pro mobilní příchozí žádosti o polohu.
- Usnadňuje účtování mezi operátory za lokalizační služby v roamingu.

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [LSCF – Location System Control Function](/mobilnisite/slovnik/lscf/)
- [SUPL – Secure User Plane for Location](/mobilnisite/slovnik/supl/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TS 23.171** (Rel-4) — LCS Stage 2 Specification for UMTS
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [LSBF na 3GPP Explorer](https://3gpp-explorer.com/glossary/lsbf/)
