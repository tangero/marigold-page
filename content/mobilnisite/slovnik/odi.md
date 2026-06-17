---
slug: "odi"
url: "/mobilnisite/slovnik/odi/"
type: "slovnik"
title: "ODI – Original Dialog Identifier"
date: 2025-01-01
abbr: "ODI"
fullName: "Original Dialog Identifier"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/odi/"
summary: "Jedinečný identifikátor používaný v IP Multimedia Subsystem (IMS) ke korelaci více souvisejících SIP dialogů nebo transakcí, které patří ke stejné komunikační relaci. Je klíčový pro kontinuitu relace,"
---

ODI je jedinečný identifikátor používaný v IMS ke korelaci více souvisejících SIP dialogů patřících ke stejné relaci za účelem kontinuity, větvení (forking) a servisní logiky.

## Popis

Original Dialog Identifier (ODI) je parametr v rámci signalizačního protokolu Session Initiation Protocol (SIP) v IP Multimedia Subsystem (IMS) podle 3GPP. Používá se k jednoznačné identifikaci počátečního SIP dialogu, který založil komunikační relaci (např. hlasový nebo videohovor). Když jsou z této původní relace vytvořeny následné SIP transakce nebo dialogy – například při přepojování hovorů, aktualizacích relace nebo scénářích větvení – nesou si s sebou parametr ODI. To umožňuje různým síťovým prvkům IMS, zejména Application Serverům ([AS](/mobilnisite/slovnik/as/)) a Serving-Call Session Control Function (S-CSCF), korelovat všechny související signalizační zprávy zpět s kontextem původní relace.

Z architektonického hlediska je ODI vkládán do SIP zpráv jádrem sítě IMS. Typicky, když počáteční požadavek INVITE vytvoří dialog, může S-CSCF nebo AS zapojený do servisní logiky přiřadit a zaznamenat ODI. Tento identifikátor je pak zahrnut do specifických polí hlaviček SIP, jako je hlavička P-Asserted-Identity nebo proprietární hlavička, v rámci následných souvisejících požadavků. Například, pokud je hovor větven (forked) na více zařízení (paralelní vyzvánění), každá větvená větev bude obsahovat ODI z původního INVITE. To umožňuje servisní logice na AS rozpoznat, že více příchozích požadavků INVITE (se stejným ODI) odpovídá stejnému původnímu pokusu o hovor, a aplikovat konzistentní směrování, účtování nebo pravidla služeb.

Jak to funguje, zahrnuje roli S-CSCF jako ukotvení stavu relace. Po přijetí počátečního požadavku INVITE pro registrovaného uživatele S-CSCF vykoná počáteční filtrační kritéria (iFC), která mohou spustit službu na AS. AS, pokud je pro korelaci relací potřeba, může vygenerovat ODI a zahrnout jej do SIP odpovědi zpět k S-CSCF. S-CSCF pak tento ODI uloží do stavu relace a zajistí jeho propagaci do všech následných SIP zpráv souvisejících s touto relací. Když je později zpracováván požadavek, jako je re-INVITE nebo REFER (pro přepojení hovoru), síťové uzly kontrolují přítomnost ODI. Používají jej k načtení správného kontextu relace, čímž zajišťují, že funkce jako přesměrování hovoru, služby během hovoru a zákonné odposlechy jsou přesně aplikovány na správnou koncová relaci, i když se signalizační cesta větvila nebo byla upravena.

## K čemu slouží

ODI byl vytvořen k řešení problému korelace relací a kontinuity služeb ve složitých signalizačních scénářích IMS. V tradiční telefonní ústředně je hovor jediný, stavový okruh. V IMS, které je založeno na SIP, může relace vytvořit více dialogů kvůli funkcím, jako je větvení hovoru (simultánní vyzvánění více zařízení), přepojení hovoru (metoda REFER) a řízení hovoru třetí stranou. Bez společného identifikátoru nemohou síťové prvky, zejména Application Servery hostující nadstavbové služby (jako záznamník, předplacené účtování nebo překlad čísel), spolehlivě spojit tyto samostatné SIP dialogy s původním hovorem. To by mohlo vést k nesprávnému provádění služeb, chybám v účtování nebo nefunkčnosti služeb.

Jeho zavedení ve Release 8 bylo motivováno rostoucí složitostí služeb IMS a potřebou robustní orchestrace služeb. Předchozí přístupy mohly spoléhat na korelaci Call-ID nebo tagů From/To, ale ty nejsou zaručeně zachovány nebo jedinečné napříč všemi větvenými větvemi nebo převedenými relacemi. ODI poskytuje stabilní, sítí přiřazený ukotvující bod. Řeší tak omezení inherentního dialogově orientovaného modelu SIP tím, že poskytuje relaci orientovaný identifikátor, a zajišťuje, že servisní logika aplikovaná na začátku hovoru (např. použití pravidla pro volání bez poplatku) zůstane správně asociována po celou dobu života hovoru, bez ohledu na to, kolik signalizačních dialogů je vytvořeno. To je zásadní pro komerční telefonní služby vyžadující přesné účtování a konzistentní chování služeb.

## Klíčové vlastnosti

- Jednoznačně identifikuje počáteční SIP dialog, který založil komunikační relaci.
- Umožňuje korelaci více větvených SIP dialogů nebo větví transakcí k jedné relaci.
- Klíčový pro konzistentní provádění servisní logiky napříč Application Servery (AS).
- Podporuje funkce kontinuity relace, jako je přepojení hovoru, přesměrování a služby během hovoru.
- Používá se S-CSCF k udržování a propagaci kontextu relace.
- Usnadňuje přesné účtování a zákonný odposlech pro složité toky hovorů.

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification

---

📖 **Anglický originál a plná specifikace:** [ODI na 3GPP Explorer](https://3gpp-explorer.com/glossary/odi/)
