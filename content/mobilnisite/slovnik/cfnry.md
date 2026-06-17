---
slug: "cfnry"
url: "/mobilnisite/slovnik/cfnry/"
type: "slovnik"
title: "CFNRY – Call Forwarding on No Reply"
date: 2025-01-01
abbr: "CFNRY"
fullName: "Call Forwarding on No Reply"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/cfnry/"
summary: "Doplňková služba, která automaticky přesměruje příchozí hovor na předem nakonfigurované číslo, když volaný účastník neodpoví v definovaném časovém úseku. Zajišťuje dokončení hovoru a zlepšuje uživatel"
---

CFNRY (přesměrování volání při neodpovědi) je doplňková služba, která přesměruje příchozí hovor na předem nastavené číslo, když volaný účastník neodpoví v definovaném časovém úseku.

## Popis

Call Forwarding on No Reply (CFNRY) je síťová doplňková služba standardizovaná v 3GPP specifikacích, především v doméně účtování a správy (TS 32.250). Funguje v servisní vrstvě jádra sítě, konkrétně jako součást servisního profilu v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) a je prováděna Mobile Switching Center ([MSC](/mobilnisite/slovnik/msc/)) nebo IP Multimedia Subsystem (IMS) Call Session Control Functions (CSCFs). Služba se aktivuje během navazování hovoru, když je zařízení volaného účastníka dosažitelné (vyzvání), ale není detekována odpověď před vypršením konfigurovatelného časovače.

Technická implementace zahrnuje několik síťových prvků. Servisní data účastníka pro CFNRY, včetně čísla pro přesměrování a hodnoty časovače neodpovědi, jsou uložena v jeho servisním profilu v HSS/HLR. Když hovor dorazí k MSC Server (v sítích s přepojováním okruhů) nebo k Serving-CSCF (v IMS), síť zkontroluje, zda je CFNRY aktivní. Pokud je aktivní, síť se pokusí upozornit volaného uživatele. Při upozornění se spustí časovač, typicky konfigurovatelný účastníkem nebo operátorem sítě (často s výchozí hodnotou např. 15-30 sekund). Pokud hovor není přijat před vypršením tohoto časovače, MSC nebo S-CSCF ukončí původní pokus o hovor a zahájí nové zřízení hovoru na předem registrované číslo pro přesměrování.

Logika služby je řízena základními stavovými modely a detekčními body definovanými v rozhraních Customized Applications for Mobile networks Enhanced Logic ([CAMEL](/mobilnisite/slovnik/camel/)) nebo IMS Service Control ([ISC](/mobilnisite/slovnik/isc/)). V IMS může být služba implementována jako initial Filter Criteria (iFC) v S-CSCF, což spouští interakci s aplikačním serverem. Pro původní pokus o hovor i pro přesměrovanou větev hovoru jsou generovány záznamy o účtování ([CDR](/mobilnisite/slovnik/cdr/)) se specifickými indikátory označujícími aktivaci CFNRY. Služba funguje ve spolupráci s dalšími variantami přesměrování hovorů (jako [CFU](/mobilnisite/slovnik/cfu/), [CFB](/mobilnisite/slovnik/cfb/), CFNRc) s definovaným pořadím priority, aby se předešlo konfliktům.

Úlohou CFNRY je zvýšit míru dokončení hovorů a uživatelský komfort. Jedná se o základní telefonní službu, která se vyvinula z legacy GSM do sítí 3G, 4G a 5G a je nyní podporována v architekturách služeb s přepojováním okruhů i v IP-based IMS. Její spolehlivý provoz závisí na přesné správě dat účastníka, precizní manipulaci s časovači a správné integraci s účtovacími systémy, aby bylo zajištěno správné účtování za přesměrovaný hovor.

## K čemu slouží

CFNRY byla vytvořena, aby vyřešila problém zmeškaných hovorů a neefektivních komunikačních pokusů. Před takovými standardizovanými službami přesměrování, pokud uživatel nezvedl telefon, volající jednoduše dostal obsazený tón nebo hlasovou schránku po vypršení časového limitu, což vyžadovalo, aby volal znovu nebo zanechal vzkaz. To bylo neefektivní pro časově citlivou komunikaci nebo když byl volaný účastník dočasně nedostupný, ale chtěl, aby se hovory dovolaly na alternativní kontakt (jako sekretářka nebo mobilní telefon). CFNRY tuto změnu směrování automatizuje a zajišťuje, že hovor dosáhne životaschopného koncového bodu bez zásahu volajícího.

Služba řeší omezení ručního zpracování hovorů a základní hlasové schránky tím, že poskytuje proaktivní, automatické dokončení hovoru. Historicky byla součástí doplňkových služeb GSM Phase 2 zavedených pro konkurenceschopnost s funkcemi pevné telefonie. Její standardizace v 3GPP (od Release 8 v kontextu rozšířených specifikací účtování) zajistila interoperabilitu napříč sítěmi a dodavateli, což umožnilo účastníkům používat stejnou službu při roamingu. Vyřešila problém dostupnosti účastníka, zvýšila využití sítě a vnímanou kvalitu služeb.

V moderních sítích zůstává CFNRY relevantní pro kontinuitu podnikání, osobní pohodlí a jako součást pokročilejších služeb obsluhy hovorů (jako screening hovorů nebo sekvenční vyzvání). Integruje se s dalšími podmínkami přesměrování, aby uživatelům poskytla detailní kontrolu nad směrováním hovorů na základě různých scénářů (obsazeno, nedostupný, neodpověď). Tato flexibilita pomáhá optimalizovat komunikační tok jak v osobním, tak podnikovém kontextu.

## Klíčové vlastnosti

- Automatické přesměrování hovoru po vypršení konfigurovatelného časovače neodpovědi
- Síťové provádění služby nevyžadující během aktivace žádnou akci od volaného účastníka
- Účastníkem konfigurovatelné cílové číslo pro přesměrování prostřednictvím síťové provisionace
- Generování specifických záznamů o účtování (CDR) pro původní a přesměrovanou větev hovoru
- Interoperabilita napříč sítěmi s přepojováním okruhů (CS) a sítěmi založenými na IMS
- Definovaná pravidla priority a interakce s ostatními službami přesměrování hovorů (CFU, CFB, CFNRc)

## Definující specifikace

- **TS 32.250** (Rel-19) — Circuit Switched Offline Charging

---

📖 **Anglický originál a plná specifikace:** [CFNRY na 3GPP Explorer](https://3gpp-explorer.com/glossary/cfnry/)
