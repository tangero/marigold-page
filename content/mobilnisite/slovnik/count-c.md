---
slug: "count-c"
url: "/mobilnisite/slovnik/count-c/"
type: "slovnik"
title: "COUNT-C – Ciphering Sequence Number for Core Network"
date: 2025-01-01
abbr: "COUNT-C"
fullName: "Ciphering Sequence Number for Core Network"
category: "Security"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/count-c/"
summary: "COUNT-C je časově proměnný parametr používaný pro synchronizaci mezi operacemi šifrování a dešifrování v sítích 3GPP. Zajišťuje kryptografickou synchronizaci mezi uživatelským zařízením (UE) a síťovým"
---

COUNT-C je časově proměnné šifrovací pořadové číslo (Ciphering Sequence Number) používané pro kryptografickou synchronizaci mezi uživatelským zařízením (UE) a prvky jádra sítě v sítích 3GPP, které zajišťuje bezpečnou a spolehlivou šifrovanou komunikaci.

## Popis

COUNT-C je klíčový bezpečnostní parametr definovaný ve specifikacích 3GPP, konkrétně v TS 33.105, který slouží jako časově proměnný vstup kryptografických algoritmů pro šifrování v doméně jádra sítě (Core Network). Funguje jako čítač, který se zvyšuje s každou šifrovanou protokolovou datovou jednotkou ([PDU](/mobilnisite/slovnik/pdu/)), čímž zajišťuje, že stejný kryptografický proud klíčů (keystream) není nikdy znovu použit se stejným šifrovacím klíčem. Parametr se skládá ze dvou hlavních složek: Hyper Frame Number ([HFN](/mobilnisite/slovnik/hfn/)) a Sequence Number ([SN](/mobilnisite/slovnik/sn/)), kde HFN představuje vyšší bity, které se zvyšují méně často, zatímco SN představuje nižší bity, které se zvyšují s každou PDU.

Architektura integrace COUNT-C zahrnuje jeho generování a správu jak v uživatelském zařízení (UE), tak v bezpečnostních entitách sítě, jako je Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) v 3G nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G. Během navázání zabezpečeného spojení oba koncové body inicializují své hodnoty COUNT-C na základě vyjednaných parametrů a následně je během relace synchronizují. Hodnota COUNT-C je kombinována s dalšími vstupy, jako je šifrovací klíč ([CK](/mobilnisite/slovnik/ck/)), identifikátor přenosového kanálu (bearer), směr přenosu a požadovaná délka proudu klíčů, aby vytvořila úplný vstup pro kryptografický algoritmus (jako je SNOW 3G, [AES](/mobilnisite/slovnik/aes/) nebo ZUC).

Během provozu pokaždé, když je PDU zašifrována pro přenos, vysílající entita zvýší svou lokální hodnotu COUNT-C a použije ji ke generování proudu klíčů, který bude XORován s nešifrovanými daty. Přijímající entita musí udržovat identickou hodnotu COUNT-C, aby vygenerovala stejný proud klíčů pro dešifrování. Pokud je synchronizace ztracena kvůli chybám přenosu nebo jiným problémům, může přijímající entita pokusit o resynchronizaci pomocí mechanismů definovaných ve specifikacích, přičemž trvalá desynchronizace obvykle vede k selhání spojení, aby se zabránilo narušení bezpečnosti.

Role COUNT-C přesahuje pouhou synchronizaci – poskytuje základní ochranu proti útokům opakováním (replay attacks) tím, že zajišťuje jedinečné zpracování každé šifrované zprávy. Protože se hodnota COUNT-C mění s každou PDU, i když útočník zachytí a zaznamená šifrovaný provoz, nemůže tyto zprávy později úspěšně zopakovat, protože hodnota COUNT-C by se mezitím posunula, což by způsobilo selhání dešifrování. Tato časově proměnná vlastnost je zásadní pro dopřednou bezpečnost (forward security) komunikační relace a je povinnou součástí všech šifrovacích algoritmů 3GPP.

## K čemu slouží

COUNT-C byl vytvořen, aby řešil základní kryptografický požadavek na časově proměnné parametry v operacích proudového šifrování v mobilních sítích. Před standardizovanými přístupy ad-hoc synchronizační mechanismy představovaly riziko kryptografických slabin, jako je opakované použití proudu klíčů, což mohlo vést k úspěšné kryptoanalýze a narušení šifrované komunikace. Bezpečnostní pracovní skupina 3GPP uznala, že robustní, standardizovaná metoda pro udržování synchronizace šifrování je nezbytná pro integritu mobilní komunikace, jak se sítě vyvíjely od 2G přes 3G a dále.

Hlavní problém, který COUNT-C řeší, je udržení dokonalé synchronizace mezi šifrujícími a dešifrujícími entitami navzdory nespolehlivé povaze bezdrátového přenosu, kde mohou být pakety ztraceny, duplikovány nebo přicházet mimo pořadí. Bez COUNT-C by i drobné synchronizační chyby způsobily katastrofické selhání komunikace, protože přijímač by generoval nesprávné proudy klíčů, což by učinilo veškerý následný provoz nedešifrovatelným. Parametr také řeší bezpečnostní požadavky tím, že zajišťuje, že stejný proud klíčů není nikdy znovu použit se stejným klíčem, což je klíčové pro prevenci určitých kryptografických útoků.

Historicky, když 3GPP zavedlo sofistikovanější kryptografické algoritmy s Release 8 a přechodem na LTE, potřeba robustního synchronizačního mechanismu se stala ještě kritičtější kvůli zvýšeným přenosovým rychlostem, různorodým typům přenosových kanálů (bearer) a složitějším síťovým architekturám. COUNT-C poskytl standardizované řešení, které mohlo fungovat napříč různými síťovými doménami (access stratum a non-access stratum) a s různými kryptografickými algoritmy, čímž zajišťoval zpětnou kompatibilitu a zároveň podporoval budoucí bezpečnostní vylepšení.

## Klíčové vlastnosti

- Časově proměnný parametr zajišťující kryptografickou synchronizaci
- Skládá se ze složek Hyper Frame Number (HFN) a Sequence Number (SN)
- Povinný vstup pro všechny šifrovací algoritmy 3GPP (SNOW 3G, AES, ZUC)
- Zabraňuje opakovanému použití proudu klíčů a chrání proti útokům opakováním (replay attacks)
- Udržuje synchronizaci i při možné ztrátě nebo přeuspořádání paketů
- Podporuje šifrovací operace pro uplink i downlink

## Definující specifikace

- **TS 33.105** (Rel-19) — 3G Security: Cryptographic Algorithm Requirements

---

📖 **Anglický originál a plná specifikace:** [COUNT-C na 3GPP Explorer](https://3gpp-explorer.com/glossary/count-c/)
