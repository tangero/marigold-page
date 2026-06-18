---
slug: "rhl"
url: "/mobilnisite/slovnik/rhl/"
type: "slovnik"
title: "RHL – Response Header Length"
date: 2002-01-01
abbr: "RHL"
fullName: "Response Header Length"
category: "Protocol"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/rhl/"
summary: "Pole protokolu definované v 3GPP TS 23.048 pro MExE, které určuje celkovou délku sekce hlavičky v oktetech v odpovědní zprávě serveru. Umožňuje přijímajícímu klientovi přesně lokalizovat začátek těla"
---

RHL (Response Header Length) je pole protokolu v 3GPP TS 23.048, které určuje celkovou délku hlavičky v oktetech v odpovědi serveru, což klientovi umožňuje lokalizovat začátek těla zprávy.

## Popis

Response Header Length (RHL) je základní pole v sadě protokolů MExE, standardizované spolu s [RHI](/mobilnisite/slovnik/rhi/) ve 3GPP Release 5. Kvantifikuje velikost části hlavičky v rámci odpovědní zprávy přenášené z MExE serveru na MExE klienta sídlícího na uživatelském zařízení (UE). Sekce hlavičky obsahuje řídicí informace, jako jsou identifikátory transakcí, bezpečnostní tokeny, typy obsahu a instrukce, které jsou oddělené od primární užitečné zátěže neboli těla zprávy (např. aplikačního souboru nebo konfiguračních dat). Hodnota RHL je vyjádřena v oktetech (bytech) a poskytuje kritický značkovač hranice.

Během provozu, když MExE klient přijme odpověď, přečte počáteční pole protokolu, která zahrnují RHI a RHL. RHL informuje protokolový zásobník klienta o tom, kolik přesně oktetů tvoří blok hlavičky. Klient poté může z příchozího bajtového proudu extrahovat přesně tento počet oktetů pro zpracování hlavičky. Jakmile je hlavička zpracována, klient ví, že následující oktety patří tělu zprávy. Tento mechanismus je zásadní pro spolehlivé rámcování zpráv, zejména při proudově orientované nebo paketové přepravě, kde hranice zpráv nejsou inherentně zachovávány. Zabrání tak třídě chyb, kdy klient mylně interpretuje data těla jako data hlavičky nebo naopak.

Technická implementace RHL podporuje hlavičky proměnné délky, což je nezbytné pro flexibilní servisní prostředí. Různé služby nebo transakce mohou vyžadovat různá množství řídicích informací. Například jednoduché potvrzení může mít krátkou hlavičku, zatímco odpověď obsahující složitý řetězec bezpečnostních certifikátů bude mít hlavičku mnohem delší. Explicitním uvedením délky se protokol vyhýbá potřebě znaků oddělovačů, které by se mohly vyskytnout v rámci binárních dat samotné hlavičky. Tento návrh je robustní a efektivní. RHL v kombinaci s RHI tvoří základní logiku parsování pro zprávy MExE, což zajišťuje, že i když se služby vyvíjejí a přidávají se nové typy hlaviček, základní mechanismus pro nalezení těla zprávy zůstává konstantní a spolehlivý.

## K čemu slouží

Účelem RHL je poskytnout jednoznačné rámcování zpráv v rámci protokolu MExE, které řeší základní problém v návrhu binárních protokolů. V raných mobilních datových službách často používaly ad-hoc protokoly hlavičky pevné délky nebo se spoléhaly na mechanismy přepravy vyšší vrstvy (jako je TCP) pro správu datových proudů. Pro efektivitu a flexibilitu v bezdrátovém prostředí s proměnlivou latencí a možným přeuspořádáním paketů je však samopopisný formát zprávy lepší. RHL umožňuje, aby každá odpověď MExE byla soběstačná; klient ji může správně zpracovat, i když přijme fragmenty zprávy nebo pokud zpracovává zprávy z vyrovnávací paměti.

To bylo zvláště důležité pro cíl MExE podporovat stahovatelné aplikace a služby, kde zprávy mohly být rozsáhlé a složité. Bez přesného indikátoru délky by klient musel prohledávat příchozí data kvůli specifickému značkovači konce hlavičky, což je neefektivní a náchylné k chybám, pokud se může sekvence značkovače vyskytnout v binárních datech hlavičky. Pole RHL poskytuje přímý a efektivní výpočet. Jeho vytvoření bylo motivováno potřebou robustní, efektivní a budoucím vývojem odolné vrstvy zasílání zpráv, která by mohla fungovat přes různé přenašeče (např. [SMS](/mobilnisite/slovnik/sms/), [GPRS](/mobilnisite/slovnik/gprs/)) definované v rámci MExE. Řešilo tak omezení dřívějších proprietárních mechanismů doručování služeb, které byly křehké a obtížně rozšiřitelné o nové funkce.

## Klíčové vlastnosti

- Určuje přesnou délku v oktetech sekce hlavičky v rámci odpovědní zprávy MExE.
- Umožňuje přesné rámcování zprávy, což klientovi dovoluje čistě oddělit data hlavičky od dat těla.
- Podporuje hlavičky proměnné délky, aby vyhověly různému množství řídicích informací na transakci.
- Odstraňuje potřebu oddělovačů v proudu dat, čímž zvyšuje robustnost parsování proti nejednoznačnosti binárních dat.
- Společně pracuje s Response Header Identifier (RHI) pro kompletní interpretaci hlavičky.
- Základní pro spolehlivý provoz přes paketově přepínané nebo zprávově orientované přenašeče používané MExE.

## Související pojmy

- [RHI – Response Header Identifier](/mobilnisite/slovnik/rhi/)

## Definující specifikace

- **TS 23.048** (Rel-5) — Secured Packets for UICC Remote Management

---

📖 **Anglický originál a plná specifikace:** [RHL na 3GPP Explorer](https://3gpp-explorer.com/glossary/rhl/)
