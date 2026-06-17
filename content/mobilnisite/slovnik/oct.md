---
slug: "oct"
url: "/mobilnisite/slovnik/oct/"
type: "slovnik"
title: "OCT – Outgoing Call Timer"
date: 2025-01-01
abbr: "OCT"
fullName: "Outgoing Call Timer"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/oct/"
summary: "Časovač v USIM, který řídí maximální dobu trvání pokusu o uskutečnění odchozího hovoru. Zabraňuje neomezeným pokusům o sestavení hovoru, čímž šetří síťové prostředky a zlepšuje uživatelský zážitek dík"
---

OCT je časovač v USIM, který omezuje délku pokusu o uskutečnění odchozího hovoru, aby zabránil neomezenému pokusu o sestavení, šetřil síťové prostředky a poskytoval včasnou zpětnou vazbu o selhání.

## Popis

Outgoing Call Timer (OCT) je časovač specifický pro účastníka, uložený v aplikaci Universal Subscriber Identity Module (USIM), jak je definováno v 3GPP TS 31.102. Jedná se o proaktivní funkci UICC (Universal Integrated Circuit Card), což znamená, že USIM může iniciovat akce nezávisle na mobilním zařízení ([ME](/mobilnisite/slovnik/me/)). Primární funkcí časovače je omezit dobu trvání procedury sestavení hovoru iniciované mobilem. Když uživatel zahájí hovor, ME odešle síti zprávu SETUP. Současně USIM spustí OCT. Pokud je hovor úspěšně sestaven (např. volaný zvedne), časovač se zastaví. Pokud se však sestavení hovoru nedokončí v předem nastavené době OCT – z důvodu přetížení sítě, nezvednutí volaného nebo jiné chyby – USIM proaktivně nařídí ME ukončit pokus o hovor. To se typicky provede odesláním terminálové odpovědi se specifickým výsledkem, jako je 'Call control by USIM', která instruuje ME k uvolnění hovoru.

Hodnota OCT je parametr definovaný v Elementary File ([EF](/mobilnisite/slovnik/ef/)) USIM v rámci tabulky telekomunikačních služeb. Konfiguruje ji operátor a lze ji personalizovat pro různé účastníky nebo tarify. Mechanismus časovače je součástí služby Call Control ([CC](/mobilnisite/slovnik/cc/)) poskytované USIM, která komunikuje s vrstvou řízení hovorů v ME prostřednictvím rozhraní Application Protocol Data Unit ([APDU](/mobilnisite/slovnik/apdu/)) definovaného [ETSI](/mobilnisite/slovnik/etsi/)/3GPP. USIM monitoruje stav hovoru zpracováním obálkových příkazů z ME, které nesou informace o stavu hovoru.

Z architektonického hlediska OCT funguje v zabezpečeném prostředí UICC, což zajišťuje odolnost logiky časovače a jeho hodnoty vůči neoprávněným zásahům. Jeho vynucování je nezávislé na síťovém jádru a poskytuje tak spolehlivý záložní mechanismus i při zpoždění nebo anomáliích v síťové signalizaci. Stanovením konečného časového limitu pro sestavení hovoru pomáhá OCT předcházet scénářům, kdy mobilní zařízení zůstane zablokováno v dlouhotrvajícím stavu sestavování hovoru, což by mohlo vybíjet baterii, zbytečně obsazovat rádiové prostředky a vést ke špatnému uživatelskému vnímání spolehlivosti služeb. Je to základní prvek role USIM v zabezpečené a efektivní správě základních telefonních služeb.

## K čemu slouží

Outgoing Call Timer byl zaveden, aby řešil problém neomezených nebo nadměrně dlouhých pokusů o sestavení hovoru v mobilních sítích. Před jeho standardizací, pokud se sestavení hovoru nezdařilo kvůli síťovým problémům nebo neodpovídajícímu volanému, mohlo mobilní zařízení zůstat ve stavu sestavování hovoru po nepředvídatelnou dobu a čekat na odpověď sítě nebo vypršení časového limitu. To plýtvalo cennými rádiovými prostředky (jako je kanál pro přenos hovoru) a životností baterie zařízení a mohlo způsobit zmatení uživatele, protože se zařízení zdálo 'zaseklé'. OCT poskytuje standardizovaný mechanismus řízený účastníkem, který tuto dobu omezuje.

Jeho zavedení bylo motivováno potřebou zlepšit efektivitu sítě a konzistentní uživatelský zážitek. Umožněním operátorům definovat maximální dobu sestavení hovoru mohou sítě rychleji uvolňovat prostředky z neúspěšných pokusů, čímž zlepšují celkovou kapacitu a stabilitu. Z pohledu uživatele zajišťuje, že neúspěšný pokus o hovor skončí v předvídatelném časovém rámci, což uživateli umožní hovor opakovat nebo provést jinou akci. Implementace časovače v zabezpečeném USIM také znamená, že jeho fungování je důvěryhodné a konzistentní napříč různými mobilními zařízeními, protože je řízeno SIM kartou poskytnutou operátorem, nikoli proměnlivým softwarem zařízení.

## Klíčové vlastnosti

- Proaktivní časovač UICC řízený aplikací USIM.
- Omezuje maximální dobu trvání pokusu o sestavení hovoru iniciovaného mobilem.
- Konfigurován mobilním operátorem v Elementary Files USIM.
- Při vypršení spustí příkaz USIM k Mobile Equipment, aby uvolnilo hovor.
- Funguje nezávisle na časových limitech na síťové straně pro vyšší spolehlivost.
- Součást standardizovaných služeb Call Control (CC) pro USIM.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 31.102** (Rel-19) — USIM Application Specification

---

📖 **Anglický originál a plná specifikace:** [OCT na 3GPP Explorer](https://3gpp-explorer.com/glossary/oct/)
