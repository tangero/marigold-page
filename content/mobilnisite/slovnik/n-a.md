---
slug: "n-a"
url: "/mobilnisite/slovnik/n-a/"
type: "slovnik"
title: "N/A – Not Applicable"
date: 2025-01-01
abbr: "N/A"
fullName: "Not Applicable"
category: "Other"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/n-a/"
summary: "Zástupný symbol nebo indikátor používaný ve specifikacích 3GPP k označení, že konkrétní parametr, pole nebo podmínka se v daném kontextu nevztahuje (není aplikovatelná). Zajišťuje jasnost protokolu a"
---

N/A je zástupný symbol používaný ve specifikacích 3GPP k explicitnímu označení, že parametr nebo podmínka se nevztahuje (není aplikovatelný), čímž zajišťuje jasnost a zabraňuje chybnému výkladu v signalizaci a konfiguraci.

## Popis

V technických specifikacích 3GPP je 'N/A' (Not Applicable – nevztahuje se) konvenční zkratka používaná k označení, že specifický parametr, informační element, pole nebo podmínka se neuplatňuje nebo není relevantní v konkrétním kontextu uvnitř protokolové zprávy, procedury nebo konfigurace. Není to technologie ani funkční entita, ale syntaktický marker používaný v tabulkách, popisech a ASN.1 definicích napříč specifikacemi, který poskytuje jednoznačné instrukce implementátorům. Jeho použití je klíčové pro zajištění interoperability, neboť objasňuje, kdy mají být určité prvky vynechány, ignorovány nebo nastaveny na rezervované hodnoty.

Použití 'N/A' se hojně vyskytuje ve specifikacích protokolových vrstev, zejména v dokumentech [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control), jako jsou 36.331 (LTE) a 38.331 (NR), které definují signalizaci mezi UE a sítí. Například v tabulkách RRC zpráv popisujících přítomnost [IE](/mobilnisite/slovnik/ie/) (Information Element) může být 'N/A' použito ve sloupci k označení, že konkrétní IE není přítomno nebo není definováno pro daný typ zprávy nebo scénář. Podobně v definicích typů ASN.1 mohou komentáře používat 'N/A' k označení, že pole se v určité verzi (release) nebo za určitých podmínek nepoužívá. Tím se předchází nejasnostem ohledně toho, zda je element volitelný, povinný, nebo prostě neexistuje.

Z architektonického hlediska 'N/A' neodpovídá žádnému síťovému uzlu, rozhraní ani signálu. Je součástí specifikačního jazyka, který definuje chování skutečných entit. Jeho role spočívá ve zjednodušení návrhu protokolu tím, že specifikacím umožňuje definovat obecné struktury, které lze přizpůsobit pro více případů použití, přičemž 'N/A' označuje neaktivní větve. Například v podmíněném příkazu popisujícím schopnosti UE mohou být některá pole označena 'N/A' pro UE, která danou funkci nepodporují, což poskytuje vodítko UE pro kódování a síti pro interpretaci.

Provozně, když specifikace uvádí, že pole je 'N/A', musí jej implementace zpracovat podle definovaných pravidel – typicky tím, že pole nezahrnou do zakódovaných zpráv, nebo přijaté hodnoty budou považovat za chyby, pokud jsou neočekávaně přítomny. Tím je zajištěno minimalizování režie protokolu a že přijímače mohou zprávy správně parsovat. Důsledné používání 'N/A' napříč verzemi 3GPP (releases) udržuje zpětnou i budoucí kompatibilitu, protože nové funkce mohou přidělit informační obsah dříve 'N/A' polím, přičemž přechod řídí verzovací mechanismy.

## K čemu slouží

Termín 'N/A' existuje, aby řešil složitost a variabilitu vlastní protokolům mobilní komunikace, které musí podporovat širokou škálu funkcí, schopností zařízení a síťových konfigurací napříč mnoha verzemi. Bez jasného způsobu označení nerelevance by se tabulky specifikací a ASN.1 moduly zanesly volitelnými prvky nebo by vyžadovaly samostatné definice pro každý dílčí scénář, což by zvýšilo riziko chybného výkladu a implementačních chyb.

Historicky, jak se specifikace 3GPP vyvíjely od verze 8 (Release 8) dále, rostla potřeba standardizovaného způsobu zpracování podmíněných a volitelných prvků. 'N/A' poskytuje stručný, všeobecně srozumitelný marker, který inženýři a generátory kódu mohou použít ke správnému vynechání polí. Řeší problém dvojznačnosti v návrhu protokolů, kde ponechání pole prázdného nebo bez komentáře by mohlo naznačovat, že je volitelné, nikoli nepoužitelné. Tato přesnost je klíčová pro testování interoperability a certifikaci.

V kontextu vývoje protokolu umožňuje 'N/A' specifikacím zachovat konzistentní strukturu a zároveň pojmout budoucí vylepšení. Pole označená 'N/A' v dřívějších verzích mohou být v pozdějších přidělena jinému účelu, přičemž marker označuje jejich předchozí nepoužívání. To podporuje rozšiřitelnost standardů 3GPP bez narušení existujících implementací, protože zařízení ignorují pole 'N/A' na základě své verze. 'N/A' je tedy základním prvkem specifikační hygieny, která podmiňuje spolehlivost a škálovatelnost systémů 3GPP.

## Klíčové vlastnosti

- Označuje nepoužitelnost (nerelevantnost) parametru nebo podmínky v konkrétních kontextech.
- Hojně používán v tabulkách specifikací RRC a v ASN.1 definicích.
- Zabraňuje nejednoznačnosti v kódování a dekódování protokolových zpráv.
- Podporuje podmíněnou přítomnost informačních elementů (IE).
- Usnadňuje údržbu specifikací napříč více verzemi (releases).
- Napomáhá automatizované generaci kódu z ASN.1 označením vynechaných polí.

## Související pojmy

- [RRC – Radio Resource Control](/mobilnisite/slovnik/rrc/)
- [LTE – Local Terminal Emulator](/mobilnisite/slovnik/lte/)
- [NR – New Radio](/mobilnisite/slovnik/nr/)

## Definující specifikace

- **TS 36.331** (Rel-19) — LTE RRC Protocol Specification
- **TS 38.331** (Rel-19) — NR Radio Resource Control (RRC) Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [N/A na 3GPP Explorer](https://3gpp-explorer.com/glossary/n-a/)
