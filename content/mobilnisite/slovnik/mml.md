---
slug: "mml"
url: "/mobilnisite/slovnik/mml/"
type: "slovnik"
title: "MML – Man-Machine Language"
date: 2025-01-01
abbr: "MML"
fullName: "Man-Machine Language"
category: "Management"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/mml/"
summary: "Textově založený příkazový jazyk používaný operátory pro správu a konfiguraci síťových prvků v telekomunikačních systémech. Poskytuje přímé, skriptovatelné rozhraní pro úlohy, jako je zřizování služeb"
---

MML je textově založený příkazový jazyk používaný operátory pro správu a konfiguraci síťových prvků v telekomunikačních systémech.

## Popis

Man-Machine Language (MML) je standardizovaný, textově založený příkazový jazyk definovaný v rámci 3GPP a dalších telekomunikačních standardů (jako [ITU-T](/mobilnisite/slovnik/itu-t/)) pro provoz, správu a údržbu síťových prvků. Slouží jako primární rozhraní mezi lidským operátorem sítě a systémy pro správu sítě nebo jednotlivými síťovými uzly, jako jsou základnové stanice (eNodeB/gNB), mobilní ústředny ([MSC](/mobilnisite/slovnik/msc/)) nebo registry domovských poloh ([HLR](/mobilnisite/slovnik/hlr/)). Příkazy MML se obvykle zadávají prostřednictvím terminálu nebo příkazového řádku ([CLI](/mobilnisite/slovnik/cli/)) připojeného k operačnímu podpůrnému systému ([OSS](/mobilnisite/slovnik/oss/)) nebo přímo na management port síťového prvku.

Syntaxe jazyka je navržena tak, aby byla stručná a jednoznačná, často se řídí strukturou sloveso-podstatné jméno s přidruženými parametry. Typický příkaz může být 'CRT SUBSCR' (Create Subscriber – Vytvořit účastníka) následovaný parametry jako [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/) a profil služby. Síťový prvek příkaz zpracuje, provede odpovídající funkci a vrátí výslednou zprávu označující úspěch nebo selhání s podrobnostmi. MML podporuje širokou škálu operací: zřizování služeb (přidávání/úprava/mazání účastníků a zařízení), konfiguraci (nastavení rádiových parametrů, směrovacích tabulek), správu poruch (získávání alarmů, resetování komponent), sledování výkonu (žádosti o čítače, spouštění trasování) a správu zabezpečení (správa přístupových pověření).

Z architektonického hlediska probíhají interakce MML často v rámci management sítě oddělené od uživatelské datové roviny z důvodu zabezpečení. Server OSS může fungovat jako prostředník, přijímá příkazy z pracovních stanic operátorů, provádí autentizaci a autorizaci a poté je předává cílovým síťovým prvkům prostřednictvím proprietárních nebo standardizovaných rozhraní, jako jsou [CORBA](/mobilnisite/slovnik/corba/) nebo SNMP. Zatímco moderní systémy stále více využívají grafická uživatelská rozhraní (GUI) a northbound RESTful API, MML zůstává klíčové pro automatizaci, skriptování a hromadné operace. Skripty obsahující sekvence příkazů MML lze napsat a spustit pro spolehlivé a rychlé provádění složitých, opakujících se úloh. Jeho role je zásadní pro každodenní zřizování služeb a odstraňování problémů, které udržují mobilní síť v chodu, a nabízí úroveň přímé kontroly a přesnosti, která je někdy nezbytná pro zkušené inženýry.

## K čemu slouží

MML bylo vytvořeno, aby řešilo kritickou potřebu jednotné, efektivní a automatizovatelné metody pro správu složitých telekomunikačních sítí s více dodavateli. V počátcích telekomunikací poskytoval každý dodavatel zařízení své vlastní proprietární management rozhraní, což nutilo operátory školit personál na více systémech a téměř znemožňovalo centralizovanou, automatizovanou správu. To zvyšovalo provozní náklady (OPEX) a riziko lidské chyby při změnách konfigurace.

Zavedení standardizovaného MML tyto problémy vyřešilo poskytnutím společného jazyka. Umožnilo operátorům vyvíjet standardizované provozní postupy a výcvikové programy nezávislé na podkladovém hardwaru. Navíc, protože je MML textově založené, je inherentně skriptovatelné. To umožnilo automatizaci rutinních úloh – jako je hromadné zřizování účastníků během akce nebo plánované zálohování konfigurace – což dramaticky zlepšilo provozní efektivitu. MML také slouží jako 'poslední záchrana', přímé rozhraní k síťovým prvkům, užitečné pro odstraňování problémů, když systémy vyšší úrovně (GUI) nejsou dostupné nebo když je vyžadována přesná, nízkonákladová kontrola. Jeho účel přetrvává v moderní éře a koexistuje s novějšími rozhraními díky své spolehlivosti, možnosti skriptování a rozsáhlé knihovně existujících provozních skriptů a odborných znalostí, které jsou kolem něj vybudovány.

## Klíčové vlastnosti

- Textově založená syntaxe příkazů pro přímou správu síťových prvků
- Podpora komplexních operací: zřizování služeb, konfigurace, správa poruch, sledování výkonu
- Umožňuje skriptování a automatizaci rutinních úloh
- Poskytuje standardizované rozhraní napříč sítěmi s více dodavateli
- Nabízí přesnou, nízkonákladovou kontrolu pro expertní odstraňování problémů
- Typicky se používá v zabezpečených prostředích operačních podpůrných systémů (OSS)

## Definující specifikace

- **TS 32.102** (Rel-19) — Telecom Management Physical Architecture Framework
- **TS 32.861** (Rel-13) — IRP Subset Selection for Network Management
- **TS 52.402** (Rel-19) — GSM Performance Management Measurements

---

📖 **Anglický originál a plná specifikace:** [MML na 3GPP Explorer](https://3gpp-explorer.com/glossary/mml/)
