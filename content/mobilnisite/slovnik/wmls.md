---
slug: "wmls"
url: "/mobilnisite/slovnik/wmls/"
type: "slovnik"
title: "WMLS – Wireless Markup Language Script"
date: 2025-01-01
abbr: "WMLS"
fullName: "Wireless Markup Language Script"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/wmls/"
summary: "Wireless Markup Language Script (WMLS) je odlehčený skriptovací jazyk navržený jako doplněk k WML, který přidává logiku na straně klienta a interaktivitu aplikacím WAP. Umožňuje základní výpočty, vali"
---

WMLS je odlehčený skriptovací jazyk, který doplňuje WML přidáním logiky na straně klienta, umožňuje základní výpočty, validaci formulářů a lokální řízení uživatelského rozhraní v rámci aplikací WAP.

## Popis

Wireless Markup Language Script (WMLS) je procedurální skriptovací jazyk založený na ECMAScriptu, avšak výrazně omezený, aby vyhovoval limitovaným možnostem raných [WAP](/mobilnisite/slovnik/wap/) telefonů. Je navržen pro vložení do [WML](/mobilnisite/slovnik/wml/) balíčků (decks) za účelem poskytnutí funkcí skriptování na straně klienta. Na rozdíl od plnohodnotného JavaScriptu má WMLS minimální knihovnu a nepodporuje dynamickou manipulaci s objektovým modelem dokumentu ([DOM](/mobilnisite/slovnik/dom/)), protože WML není založeno na DOM. Místo toho skripty WMLS fungují v kontextu WML karty, manipulují s proměnnými, řídí navigaci a provádějí jednoduchou validaci vstupů.

WMLS funguje tak, že je deklarován v rámci WML balíčku pomocí elementu `<wmls>`. Zdrojový kód skriptu je kompilován do kompaktní binární podoby (WMLScript bytecode) pro přenos přes bezdrátovou síť na klientské zařízení. Tuto kompilaci může provést WAP brána nebo původní server. Na straně klienta obsahuje WML mikroprohlížeč interpret WMLScript. Když je načtena WML karta, která vyvolá skript, interpret spustí bytecode. Ke skriptům lze přistupovat prostřednictvím [URL](/mobilnisite/slovnik/url/) (např. `wmls://`) nebo je lze spouštět událostmi v rámci WML. Typickými případy použití jsou kontrola formátu vstupního pole před jeho odesláním na server, provedení jednoduchého aritmetického výpočtu lokálně nebo řízení následně zobrazené karty na základě volby uživatele.

Klíčovými komponentami WMLS jsou syntaxe skriptovacího jazyka a standardní knihovny (např. pro práci s řetězci, čísly s plovoucí řádovou čárkou, dialogy, URL a funkce WML prohlížeče), kompilátor převádějící zdrojový kód na bytecode a interpret v klientském mikroprohlížeči. Jeho úlohou v síti bylo přidání vrstvy inteligence a efektivity službám WAP. Tím, že umožnil část zpracování na straně klienta, snížil zbytečné síťové transakce (jako odesílání neplatných dat) a umožnil responsivnější uživatelská rozhraní, což v rámci těsných technologických omezení učinilo rané mobilní aplikace o něco dynamičtějšími a uživatelsky přívětivějšími.

## K čemu slouží

WMLS byl vytvořen, aby vyřešil konkrétní nedostatek původní specifikace [WAP](/mobilnisite/slovnik/wap/) 1.x, která obsahovala pouze statický obsahový jazyk [WML](/mobilnisite/slovnik/wml/). Zatímco WML umožňovalo definovat formuláře a navigaci, jakákoli logika – například ověření, že pole telefonního čísla obsahuje pouze číslice – vyžadovala přenos na server a zpět. To bylo neefektivní na pomalých bezdrátových připojeních s vysokou latencí a vedlo ke špatné uživatelské zkušenosti. Účelem WMLS bylo zavést bezpečný a odlehčený mechanismus pro logiku na straně klienta.

Problém řešil tím, že poskytl okleštěný skriptovací jazyk, který mohl běžet na omezené paměti a procesoru mobilních telefonů. Jazyk byl navržen jako bezpečný (bez přístupu k hardwaru zařízení nebo souborovému systému) a kompaktní (jak ve velikosti zdrojového kódu, tak v kompilovaném bytecode). To vývojářům umožnilo vytvářet WAP aplikace, které byly interaktivnější a efektivnější, a zlepšit tak použitelnost služeb jako mobilní bankovnictví, rezervační systémy nebo informační portály. Rozšířil možnosti platformy WAP, aniž by vyžadoval výkonnější zařízení nebo rychlejší sítě, a překlenul tak mezeru do doby, než se na mobilních zařízeních staly životaschopnými pokročilejší technologie, jako je [XHTML](/mobilnisite/slovnik/xhtml/) Mobile Profile a plnohodnotný JavaScript.

## Klíčové vlastnosti

- Syntaxe založená na ECMAScriptu s omezenou funkcionalitou pro mobilní zařízení
- Kompilace do kompaktního bytecode (WMLScript) pro efektivní přenos
- Standardní knihovny pro funkce práce s řetězci, čísly s plovoucí řádovou čárkou, dialogy, URL a WML prohlížečem
- Bezpečné prováděcí prostředí bez přístupu k prostředkům zařízení
- Vyvolání pomocí URL nebo vazeb na události WML v rámci balíčku (decku)
- Umožňuje validaci vstupů na straně klienta, lokální výpočty a řízení navigace

## Související pojmy

- [WML – Wireless Mark-up Language](/mobilnisite/slovnik/wml/)
- [WAP – Wireless Application Protocol](/mobilnisite/slovnik/wap/)

## Definující specifikace

- **TS 23.057** (Rel-19) — Mobile Execution Environment (MExE) Specification

---

📖 **Anglický originál a plná specifikace:** [WMLS na 3GPP Explorer](https://3gpp-explorer.com/glossary/wmls/)
