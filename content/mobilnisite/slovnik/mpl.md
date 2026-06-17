---
slug: "mpl"
url: "/mobilnisite/slovnik/mpl/"
type: "slovnik"
title: "MPL – Multiplex Payload Length"
date: 2025-01-01
abbr: "MPL"
fullName: "Multiplex Payload Length"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/mpl/"
summary: "Parametr ve specifikacích kodeků 3GPP, který definuje délku přenášených dat (payload) v rámci multiplexovaného datového rámce. Je klíčový pro správné sestavení a zpracování paketů hlasových a zvukovýc"
---

MPL je parametr ve specifikacích kodeků 3GPP, který definuje délku přenášených dat (payload) v rámci multiplexovaného datového rámce, čímž zajišťuje správné sestavení a zpracování hlasových a zvukových paketů pro interoperabilitu.

## Popis

Multiplex Payload Length (MPL) je technický parametr definovaný ve specifikacích 3GPP pro hlasové a multimediální kodeky, zejména v kontextu kodeků Adaptive Multi-Rate ([AMR](/mobilnisite/slovnik/amr/)) a AMR-Wideband, jak je specifikováno v TS 26.110. Odkazuje na přesnou délku, v bitech nebo bajtech, zakódovaných hlasových dat (payload), které jsou přenášeny v rámci specifického formátu multiplexovaného rámce. Tyto multiplexované rámce se používají pro přenos komprimovaných hlasových dat přes rozhraní vzduchu a přes páteřní síť mezi mobilním terminálem a převodníkem (transcoderem) v síti. MPL není jediná pevná hodnota, ale liší se v závislosti na režimu kodeku (přenosové rychlosti) a typu používaného rámce.

Jeho funkce je nedílnou součástí činnosti kodeku. Hlasový kodér v mobilním telefonu vytvoří pro každý hlasový rámec (obvykle 20 ms) blok zakódovaných dat. Tento blok dat, představující komprimované hlasové parametry, je hlavní přenášenou částí (payload). Pro přenos však musí být tato část zabalena společně s dodatečnými řídicími informacemi, bity pro detekci chyb a případně výplní (padding), aby vytvořila úplný rámec vyhovující požadavkům transportní vrstvy. Multiplexní vrstva tento rámec sestavuje a MPL definuje velikost segmentu hlavní přenášené části v něm. Přijímající entita (např. dekodér nebo převodník) používá známý MPL, který je často implicitně signalizován typem rámce nebo explicitně v hlavičce, aby správně extrahovala bity přenášené části z přijatého rámce před dekódováním.

Klíčové komponenty zahrnující MPL zahrnují samotný hlasový kodek (např. [AMR-NB](/mobilnisite/slovnik/amr-nb/), [AMR-WB](/mobilnisite/slovnik/amr-wb/)), definice struktury rámce a související řídicí protokoly. Například v kodeku AMR existuje osm režimů zdrojového kodeku s různými přenosovými rychlostmi, z nichž každý vede k jiné velikosti přenášené části. MPL pro každý režim je přesně definován. Struktura rámce pro rozhraní Iu (mezi RNC a páteřní sítí) a rozhraní Um (přes vzduch) má navíc své vlastní multiplexní schémata, kde je MPL kritickým polem. Jeho úlohou je zajistit jednoznačnou interpretaci datového toku; nesprávná hodnota MPL by vedla k chybnému zarovnání při zpracování, což by způsobilo poškozené dekódování hlasu nebo úplné selhání hlasového hovoru. Je to základní část specifikace interoperability, která zaručuje, že zařízení od různých výrobců si mohou úspěšně vyměňovat zakódovaný hlas.

## K čemu slouží

Parametr Multiplex Payload Length existuje proto, aby řešil problém spolehlivého přenosu proměnně rychlých zakódovaných hlasových dat strukturovaným a předvídatelným způsobem přes různá síťová rozhraní. V raných digitálních celulárních systémech byl hlas často kódován pevnou rychlostí, což vedlo k jednoduššímu rámcování. Příchod pokročilejších kodeků, jako je [AMR](/mobilnisite/slovnik/amr/), které dynamicky vybírají nejlepší přenosovou rychlost na základě stavu kanálu, zavedl proměnlivost ve velikosti bloku zakódovaného hlasu. Tato proměnlivost vytvořila potřebu jasné, standardizované definice toho, jaká část přenášeného rámce představuje skutečnou hlasovou část oproti režijním datům.

Historicky by bez přesně definovaného MPL byla interoperabilita mezi síťovými prvky od různých výrobců obtížná. Zařízení jednoho výrobce mohlo interpretovat strukturu rámce mírně odlišně než zařízení jiného, což vedlo k selhání navázání hovoru nebo špatné kvalitě hlasu. Specifikace MPL v normách jako TS 26.110 tuto přesnou definici poskytuje. Řeší omezení ad-hoc metod rámcování tím, že nařizuje konzistentní interpretaci multiplexovaného datového toku. To je obzvláště kritické v mobilních sítích, kde rámce procházejí více síťovými segmenty (terminál, základnová stanice, radiový síťový řadič, mediální brána), z nichž každý může potřebovat hlasová data zpracovat, převést nebo přeposlat. MPL zajišťuje, že každá entita v řetězci přesně ví, kde přenášená část začíná a končí, což umožňuje bezproblémový provoz a usnadňuje funkce jako provoz bez tandemového spojení (TFO) a provoz bez převodníku (TrFO) tím, že umožňuje přesnou manipulaci s datovým tokem.

## Klíčové vlastnosti

- Definuje přesnou délku hlavní přenášené části (payload) kodeku v rámci multiplexovaného rámce
- Jeho hodnota závisí na konkrétním používaném režimu kodeku (přenosové rychlosti) (např. AMR 4,75 kbps vs 12,2 kbps)
- Nezbytný pro správné zpracování a extrakci hlasových dat dekodéry a převodníky
- Specifikován v bitech nebo oktetech v příslušných tabulkách specifikací kodeků 3GPP
- Klíčový parametr pro zajištění kompletní interoperability hlasových služeb
- Používá se ve strukturách rámců pro rozhraní radiové části (Um) i páteřní sítě (Iu, Nb)

## Související pojmy

- [AMR – Adaptive Multi-Rate](/mobilnisite/slovnik/amr/)
- [AMR-WB – Adaptive Multi-Rate Wideband Speech Codec](/mobilnisite/slovnik/amr-wb/)

## Definující specifikace

- **TS 26.110** (Rel-19) — 3G-324M Multimedia Codecs for Circuit Switched Networks

---

📖 **Anglický originál a plná specifikace:** [MPL na 3GPP Explorer](https://3gpp-explorer.com/glossary/mpl/)
