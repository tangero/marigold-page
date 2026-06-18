---
slug: "udhl"
url: "/mobilnisite/slovnik/udhl/"
type: "slovnik"
title: "UDHL – User Data Header Length"
date: 2002-01-01
abbr: "UDHL"
fullName: "User Data Header Length"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/udhl/"
summary: "8bitové pole, které udává celkovou délku (v bajtech) hlavičky uživatelských dat (User Data Header) v SMS zprávě. Bezprostředně následuje po indikátoru UDHI a je klíčové pro správné zpracování informač"
---

UDHL je 8bitové pole udávající celkovou délku hlavičky uživatelských dat (User Data Header) v bajtech v SMS zprávě, které umožňuje správné zpracování informačních prvků hlavičky před textem zprávy.

## Popis

Délka hlavičky uživatelských dat (User Data Header Length, UDHL) je nedílnou součástí mechanismu hlavičky uživatelských dat ([UDH](/mobilnisite/slovnik/udh/)) v [SMS](/mobilnisite/slovnik/sms/), definovaného ve specifikaci 3GPP TS 23.040. Jedná se o 8bitovou (jednobajtovou) hodnotu, která zaujímá první bajt pole TP-User-Data, je-li indikátor hlavičky uživatelských dat ([UDHI](/mobilnisite/slovnik/udhi/)) nastaven na 1. Jediným účelem UDHL je deklarovat celkovou délku celé následující hlavičky uživatelských dat v bajtech. Tato hodnota délky zahrnuje všechny následující informační prvky (IEs), ale nezahrnuje samotný bajt UDHL ani text uživatelských dat. Rozsah je od 0 do 140 bajtů, omezený maximální velikostí užitečného zatížení SMS.

Při provozu, když entita SMS (např. mobilní zařízení nebo [SMSC](/mobilnisite/slovnik/smsc/)) zpracovává zprávu s UDHI=1, přečte první bajt pole TP-User-Data jako UDHL. Tato hodnota sděluje parseru, kolik bajtů má zpracovat jako strukturovanou UDH. Například, je-li UDHL rovno 5, dalších 5 bajtů je interpretováno jako hlavička. Parser poté sekvenčně dekóduje obsah hlavičky, který se skládá z jednoho nebo více informačních prvků. Každý [IE](/mobilnisite/slovnik/ie/) je složen z identifikátoru informačního prvku ([IEI](/mobilnisite/slovnik/iei/)), délky dat informačního prvku (IEDL) a vlastních dat ([IED](/mobilnisite/slovnik/ied/)). Součet délek všech IE se musí přesně rovnat hodnotě UDHL. Po přečtení UDHL bajtů jsou zbývající bajty v poli TP-User-Data považovány za užitečné zatížení textu.

Z architektonického hlediska slouží UDHL jako klíčový ukazatel, který definuje hranici mezi řídicími informacemi a uživatelskými daty v rámci užitečného zatížení SMS. Umožňuje hlavičky proměnné délky bez nutnosti pevného formátu, což poskytuje značnou flexibilitu. Protokolový zásobník SMS v síti nebo v zařízení se spoléhá na přesnou hodnotu UDHL, aby správně oddělil hlavičku před zobrazením zprávy uživateli nebo předáním aplikaci. Nesprávná hodnota UDHL by způsobila chybné zpracování, což by mohlo vést ke zkaženému zobrazení zprávy nebo nerozpoznání funkcí hlavičky. Jeho návrh je jednoduchý, ale účinný, a tvoří páteř rozšiřitelné architektury UDH tím, že umožňuje spojení více různých IE v jedné zprávě a zároveň jasně vymezuje jejich společný rozsah.

## K čemu slouží

UDHL bylo vytvořeno, aby vyřešilo potřebu flexibilního systému hlaviček proměnné délky v rámci přísných omezení velikosti [SMS](/mobilnisite/slovnik/sms/) zprávy. Rané SMS neměly koncept hlavičky; všech 160 znaků (nebo 140 bajtů) bylo určeno pro uživatelský text. Pro zavedení funkcí, jako je spojování zpráv, kdy je dlouhá zpráva rozdělena do několika segmentů SMS, byla potřeba metoda pro vložení číslování a identifikace segmentů do zprávy bez poškození viditelného textu. Hlavička pevné délky by byla neefektivní a nepružná pro budoucí funkce. UDHL poskytuje dynamické řešení: sděluje příjemci přesně to, jaká část užitečného zatížení je vyhrazena pro informace hlavičky, bez ohledu na to, kolik nebo jaké typy informačních prvků jsou přítomny.

Tím se řeší problém rozšiřitelnosti a souběžné existence více rozšířených funkcí v jedné zprávě. Například zpráva může obsahovat jak IE pro spojování, tak IE pro aplikační port. UDHL umožňuje příjemci správně najít konec této složené hlavičky. Bez UDHL by příjemce neměl způsob, jak zjistit, kde hlavička končí a kde text začíná, protože IE mohou mít proměnnou délku dat. Motivací bylo vytvořit v rámci SMS budoucím potřebám odolnou strukturu typu TLV (Type-Length-Value), která umožňuje kontinuální inovace v službách zasílání zpráv – jako jsou vyzváněcí tóny, obrázky (přes EMS) a WAP push – při zachování jediného jednoduchého pole délky pro zpracování.

Jeho zavedení spolu s UDHI standardizovalo dříve roztříštěný prostor proprietárních implementací. Poskytnutím jasného a jednoznačného ukazatele délky zajistilo interoperabilitu mezi zařízeními a síťovým vybavením různých výrobců. To bylo klíčové pro globální zavádění interoperabilních přidaných služeb přes SMS, což z ní učinilo spolehlivou platformu pro doručování služeb. Mechanismus UDHL je příkladem efektivního využití omezeného prostoru užitečného zatížení k umožnění bohaté funkcionality.

## Klíčové vlastnosti

- 8bitové pole délky definující celkovou velikost UDH v bajtech
- První bajt pole TP-User-Data při nastaveném UDHI
- Umožňuje zpracování hlaviček uživatelských dat (UDH) proměnné délky
- Klíčové pro oddělení informačních prvků (IEs) hlavičky od užitečného zatížení textu
- Podporuje více spojených informačních prvků
- Definovaný rozsah 0–140 bajtů omezený limity užitečného zatížení SMS

## Související pojmy

- [UDHI – User Data Header Indicator](/mobilnisite/slovnik/udhi/)
- [UDH – User Data Header](/mobilnisite/slovnik/udh/)
- [SMS – Short Message Service](/mobilnisite/slovnik/sms/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [UDHL na 3GPP Explorer](https://3gpp-explorer.com/glossary/udhl/)
