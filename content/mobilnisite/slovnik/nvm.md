---
slug: "nvm"
url: "/mobilnisite/slovnik/nvm/"
type: "slovnik"
title: "NVM – Non-Volatile Memory"
date: 2025-01-01
abbr: "NVM"
fullName: "Non-Volatile Memory"
category: "Other"
segment: "Testing"
canonical: "https://3gpp-explorer.com/glossary/nvm/"
summary: "NVM (nevolatilní paměť) je trvalé úložiště, které uchovává data bez napájení a používá se v uživatelském zařízení (UE) 3GPP pro ukládání konfiguračních a provozních dat. Je základní hardwarovou kompon"
---

NVM (nevolatilní paměť) je trvalá paměťová hardwarová komponenta v uživatelském zařízení 3GPP, která uchovává data bez napájení pro konfigurační a provozní údaje, čímž zajišťuje funkčnost zařízení a síťovou konektivitu.

## Popis

NVM (nevolatilní paměť) v kontextu specifikací 3GPP označuje trvalé paměťové hardwarové úložiště integrované do uživatelského zařízení (UE), jako jsou chytré telefony, tablety a IoT zařízení. Na rozdíl od volatilní paměti (např. [RAM](/mobilnisite/slovnik/ram/)) si NVM uchovává uložené informace i po vypnutí zařízení. Tato vlastnost je klíčová pro udržování základních parametrů zařízení, nastavení síťové konfigurace, dat modulu [SIM](/mobilnisite/slovnik/sim/), firmwaru a provozních logů. Technické specifikace 3GPP, zejména v řadě 34 (testování shody UE) a 35 (bezpečnostní algoritmy), definují požadavky a testovací postupy, které zajišťují, že komponenty NVM splňují standardy pro integritu dat, odolnost (počet cyklů zápisu/mazání), dobu uchování dat a spolehlivost za různých podmínek prostředí.

Z architektonického hlediska je NVM klíčovou komponentou hardwarové platformy UE, která komunikuje se základnovým procesorem zařízení, aplikačním procesorem a dalšími podsystémy. Typicky ukládá mezinárodní identifikaci mobilního zařízení ([IMEI](/mobilnisite/slovnik/imei/)), schopnosti rádiového přístupu, seznamy preferovaných sítí, bezpečnostní klíče a firmware pro modem a protokolové zásobníky. Paměť je spravována specializovanými řadiči a softwarovými vrstvami, které zajišťují operace čtení/zápisu, vyrovnávání opotřebení (pro prodloužení životnosti paměti), opravu chyb a šifrování dat pro bezpečnost. V testovacích specifikacích, jako jsou 34.131 a 35.934, 3GPP popisuje shodové testy výkonu NVM, včetně testů uchování dat po cyklech napájení, testů odolnosti při opakovaných zápisech a ověření mechanismů zabezpečeného úložiště.

Role NVM v síťovém ekosystému je základní, ale nepřímá; umožňuje UE trvale ukládat potřebné informace pro úspěšné připojení a provoz v sítích 3GPP (od 2G do 5G). Například uchovává informace o schopnostech UE, které jsou hlášeny síti během registrace a ovlivňují přidělování síťových zdrojů a poskytování služeb. Spolehlivá NVM zajišťuje, že se UE může po restartu obnovit do předchozího stavu, udržovat nepřetržitý provoz a bezpečně ukládat citlivé přihlašovací údaje. Ačkoli se nejedná o síťovou funkci jako takovou, její standardizovaný výkon je klíčový pro celkovou spolehlivost systému, uživatelský zážitek a bezpečnost, protože poškozené nebo nespolehlivé úložiště může vést k neúspěšným připojením k síti, výpadkům služeb nebo bezpečnostním slabinám.

## K čemu slouží

Účelem specifikace NVM (nevolatilní paměti) ve standardech 3GPP je zajistit interoperabilitu, spolehlivost a bezpečnost uživatelských zařízení napříč různými výrobci a síťovými operátory. Před standardizací mohla nekonzistentní kvalita a výkon paměti vést k poruchám zařízení, ztrátě dat nebo narušení bezpečnosti, což podkopávalo spolehlivost sítě a důvěru uživatelů. Definováním požadavků na shodové testy ve specifikacích, jako jsou 34.131 a 35.934, poskytuje 3GPP společný referenční rámec pro hardwarovou NVM, který zajišťuje, že všechna kompatibilní UE splňují minimální prahové hodnoty pro uchování dat, odolnost a zabezpečené úložiště.

Historicky, jak se mobilní zařízení vyvíjela od základních telefonů ke složitým chytrým telefonům a IoT zařízením, množství a důležitost ukládaných dat dramaticky vzrostly. Raná zařízení ukládala minimální konfiguraci, ale moderní UE vyžadují trvalé úložiště pro složité protokolové zásobníky, multimédia, aplikace a citlivá data účastníka. Motivací pro specifikace NVM byla potřeba zajistit, aby toto úložiště bylo dostatečně robustní, aby odolalo reálným vzorcům používání – jako je časté zapínání/vypínání, teplotní výkyvy a dlouhá období nečinnosti – aniž by došlo ke zkreslení základních síťových parametrů. Tato spolehlivost je zásadní pro plynulou mobilitu, protože se UE musí po vypnutí nebo přesunu mezi oblastmi pokrytí rychle znovu připojit k sítím pomocí uložených přihlašovacích údajů a nastavení.

Specifikace NVM dále řeší bezpečnostní obavy tím, že vyžadují schopnosti pro chráněné ukládání kryptografických klíčů a identit účastníků. Bez spolehlivého nevolatilního úložiště by mohly být bezpečnostní mechanismy, jako je autentizace a šifrování, ohroženy, pokud by došlo ke ztrátě nebo poškození klíčů. NVM tedy tvoří základ důvěryhodného modelu sítí 3GPP, protože zajišťuje, že každé zařízení může bezpečně a trvale udržovat svou identitu a autorizovaný stav. Zatímco samotná technologie NVM (např. Flash paměť) se vyvíjí nezávisle, standardy 3GPP zajišťují, že její použití v telekomunikacích splňuje přísné požadavky globálních mobilních sítí.

## Klíčové vlastnosti

- Trvalé uchování dat bez elektrického napájení
- Úložiště pro konfiguraci UE a síťové parametry
- Zabezpečené úložiště pro kryptografické klíče a identity
- Odolnost vůči opakovaným cyklům zápisu/mazání
- Dlouhodobé uchování dat po stanovená období
- Shoda se standardizovanými testovacími postupy

## Související pojmy

- [UE – User Equipment](/mobilnisite/slovnik/ue/)
- [IMEI – International Mobile Station Equipment Identities](/mobilnisite/slovnik/imei/)
- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)

## Definující specifikace

- **TS 34.131** (Rel-19) — SIM API C Language Test Specification
- **TR 35.934** (Rel-19) — Tuak algorithm set for 3GPP auth & key gen

---

📖 **Anglický originál a plná specifikace:** [NVM na 3GPP Explorer](https://3gpp-explorer.com/glossary/nvm/)
