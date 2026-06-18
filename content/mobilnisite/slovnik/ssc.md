---
slug: "ssc"
url: "/mobilnisite/slovnik/ssc/"
type: "slovnik"
title: "SSC – Supplementary Service Control string"
date: 2026-01-01
abbr: "SSC"
fullName: "Supplementary Service Control string"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ssc/"
summary: "Řetězec pro řízení doplňkových služeb (SSC) je posloupnost znaků (čísel a symbolů), kterou mobilní účastník používá k přímé aktivaci, deaktivaci nebo dotazování na doplňkovou službu ze svého telefonní"
---

SSC je standardizovaný řetězec znaků, začínající znakem '*' nebo '#', který mobilní účastník používá k přímé aktivaci, deaktivaci nebo dotazování na doplňkovou službu (např. přesměrování hovoru) ze svého telefonního přístroje.

## Popis

Řetězec pro řízení doplňkových služeb (SSC) je uživatelsky přívětivý, vyvolatelný formát řetězce standardizovaný ve specifikacích 3GPP (např. TS 24.526, TS 29.508) pro ovládání doplňkových služeb. Jedná se o rozhraní mezi člověkem a strojem, které umožňuje účastníkovi vydávat příkazy síti pro správu služeb, jako je Bezpodmínečné přesměrování hovoru ([CFU](/mobilnisite/slovnik/cfu/)), Zákaz hovorů ([BAOC](/mobilnisite/slovnik/baoc/)) nebo Čekání na hovor ([CW](/mobilnisite/slovnik/cw/)). Typický SSC má strukturovanou syntaxi: předponu (často '*' nebo '#'), kód služby (dvoumístné číslo identifikující službu, např. 21 pro CFU), operační kód (jedna číslice pro aktivaci, deaktivaci, registraci, vymazání nebo dotaz) a volitelně doplňkové informace, jako je cílové telefonní číslo nebo heslo. Například **21*+123456789# může aktivovat CFU na číslo +123456789.

Když uživatel vyvolá SSC a stiskne tlačítko pro odeslání/hovor, mobilní přístroj jej nezpracovává jako běžný telefonní hovor. Místo toho zabalí řetězec do signalizační zprávy, konkrétně do zprávy FACILITY nebo REGISTER v rámci protokolu řízení hovoru, jako je [DTAP](/mobilnisite/slovnik/dtap/) (Direct Transfer Application Part). Tato zpráva je odeslána přes rozhraní rádiového přístupu k [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Centre). Funkce řízení hovoru v MSC zprávu přijme, parsuje SSC podle standardizované syntaxe a interpretuje požadovanou operaci. MSC následně komunikuje s příslušnými síťovými databázemi – především s [VLR](/mobilnisite/slovnik/vlr/) (Visitor Location Register) a [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register) – aby příkaz provedla. Pro registraci nebo dotaz může MSC komunikovat s HLR přes [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) a aktualizovat nebo načíst profil služeb účastníka.

Mechanismus SSC funguje ve spojení se služební logikou sítě. Pro základní služby může SSC zpracovat MSC přímo. U pokročilejších služeb nebo těch zahrnujících CAMEL řízení může MSC zapojit gsmSCF. Standardizace syntaxe SSC zajišťuje interoperabilitu mezi přístroji jakéhokoli výrobce a sítěmi jakéhokoli operátora, což poskytuje konzistentní uživatelský zážitek po celém světě. Je to klíčová součást rozhraní mezi člověkem a strojem (MMI) pro telekomunikační služby. Zatímco moderní smartphony často spravují tyto služby prostřednictvím grafických menu nebo aplikací, tato rozhraní nakonec generují standardizované SSC řetězce pro přenos do sítě, čímž zajišťují zpětnou kompatibilitu.

## K čemu slouží

Řetězec pro řízení doplňkových služeb (SSC) byl vytvořen, aby poskytl jednoduchou, jednotnou a uživatelsky přívětivou metodu pro ovládání síťových funkcí. Před jeho standardizací mohla aktivace služeb, jako je přesměrování hovorů, vyžadovat volání na zákaznickou podporu nebo použití proprietárních, operátorově specifických kódů, což vedlo ke špatné uživatelské zkušenosti a omezovalo mobilitu účastníků mezi různými sítěmi. Standard SSC tento problém vyřešil definováním univerzálního, vyvolatelného kódového jazyka, který funguje na jakémkoli GSM/UMTS/LTE/5G telefonu v jakékoli kompatibilní síti.

Jeho primárním účelem je umožnit účastníkovi samostatnou provizi a správu doplňkových služeb. Tím se snižují provozní náklady síťových operátorů minimalizací volání na zákaznická centra pro jednoduché změny služeb. Zároveň to posiluje postavení uživatelů a dává jim okamžitou kontrolu nad jejich telefonními funkcemi. Strukturovaná syntaxe s oddělenými poli pro službu, operaci a parametry umožňuje ovládání širokého spektra služeb prostřednictvím konzistentního a zapamatovatelného vzoru (např. *21* pro přesměrování, *33* pro zákaz).

Historicky byl koncept SSC představen v raných standardech GSM (R99) a byl zachován ve všech následujících vydáních včetně 5G. Jeho dlouhověkost je dokladem jeho účinnosti jako jednoduchého, ale výkonného mechanismu uživatelského rozhraní. Zatímco se objevily nové metody provize, jako je OMA DM (Open Mobile Alliance Device Management) nebo HTTP rozhraní (pro 5G), SSC zůstává základní záložní a široce srozumitelnou metodou pro řízení služeb, která zajišťuje přístupnost a interoperabilitu napříč desetiletími vývoje mobilních technologií.

## Klíčové vlastnosti

- Standardizovaný formát vyvolatelného řetězce pro uživatelské řízení služeb
- Používá syntaxi s předponou, kódem služby, operačním kódem a parametry
- Umožňuje aktivaci, deaktivaci, registraci, vymazání a dotazování služeb
- Přenášen signalizací řízení hovoru (např. zprávou FACILITY) k MSC
- Poskytuje konzistentní uživatelský zážitek ve všech sítích a na všech přístrojích
- Podporuje širokou škálu doplňkových služeb (přesměrování hovorů, zákazy, čekání atd.)

## Související pojmy

- [MMI – Man Machine Interface](/mobilnisite/slovnik/mmi/)
- [DTAP – Direct Transfer Application Part](/mobilnisite/slovnik/dtap/)
- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3
- **TS 25.211** (Rel-19) — UTRA FDD Layer 1: Transport & Physical Channels
- **TS 25.213** (Rel-19) — UTRA FDD Spreading and Modulation
- **TR 26.803** (Rel-17) — 5G Media Streaming Extensions for Edge Processing
- **TS 26.891** (Rel-16) — Media Distribution Services in 5G System
- **TR 28.844** (Rel-18) — Technical Report on Charging Aspects of Satellite in 5GS
- **TS 29.109** (Rel-19) — GAA Bootstrapping Interfaces (Zh, Dz, Zn, Zpn)
- **TS 29.508** (Rel-19) — 5G Session Management Event Exposure Service
- **TS 29.512** (Rel-19) — 5G Session Management Policy Control Service
- **TS 29.514** (Rel-19) — 5G System; Policy Authorization Service; Stage 3
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.525** (Rel-19) — 5G UE Policy Control Service Stage 3
- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks
- … a dalších 6 specifikací

---

📖 **Anglický originál a plná specifikace:** [SSC na 3GPP Explorer](https://3gpp-explorer.com/glossary/ssc/)
