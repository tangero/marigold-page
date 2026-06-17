---
slug: "fplmn"
url: "/mobilnisite/slovnik/fplmn/"
type: "slovnik"
title: "FPLMN – Forbidden Public Land Mobile Network"
date: 2025-01-01
abbr: "FPLMN"
fullName: "Forbidden Public Land Mobile Network"
category: "Identifier"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/fplmn/"
summary: "Seznam zakázaných veřejných pozemních mobilních sítí (FPLMN) je uložený záznam na SIM/USIM kartě uživatelského zařízení (UE). Obsahuje kombinace mobilního kódu země (MCC) a mobilního kódu sítě (MNC) s"
---

FPLMN je seznam uložený na SIM/USIM karty uživatelského zařízení (UE), který obsahuje kombinace MCC a MNC sítí, na které se UE nesmí dočasně automaticky připojit ani se na ně registrovat.

## Popis

Seznam zakázaných veřejných pozemních mobilních sítí (FPLMN) je klíčová datová struktura na straně účastníka a zařízení definovaná ve specifikacích 3GPP, včetně TS 21.905 (slovní zásoba), TS 22.811 (aspekty USIM) a TS 31.121 (testovací specifikace USIM). Je uložen v nevolatilní paměti modulu univerzální účastnické identity (USIM) nebo SIM karty uvnitř uživatelského zařízení (UE). Každá položka v seznamu je identifikátor PLMN, který se skládá z mobilního kódu země ([MCC](/mobilnisite/slovnik/mcc/)) a mobilního kódu sítě ([MNC](/mobilnisite/slovnik/mnc/)). Primární funkcí tohoto seznamu je zabránit UE v plýtvání časem a energií baterie opakovanými pokusy o registraci u sítě, která ji již dříve odmítla.

Mechanismus funguje následovně: Když UE provádí proceduru registrace (připojení) nebo aktualizace polohy u navštívené sítě PLMN (VPLMN), může síť odpovědět zamítavou zprávou. Pokud toto zamítnutí obsahuje specifickou příčinnou hodnotu indikující trvalou nebo polotrvalou chybu (např. 'PLMN not allowed', '[GPRS](/mobilnisite/slovnik/gprs/) not allowed in this PLMN', 'No suitable cells in location area'), vrstva správy mobility v UE přidá identifikátor této sítě PLMN (MCC+MNC) do seznamu FPLMN uloženého na USIM. Během následných automatických procesů výběru sítě – například při zapnutí UE, ztrátě pokrytí nebo návratu ze zahraničí – je algoritmus výběru sítě v UE povinen vyloučit ze sady kandidátských sítí pro automatický výběr jakoukoli síť PLMN, jejíž ID se nachází v seznamu FPLMN.

Seznam FPLMN je spravován jak UE, tak sítí. UE přidává položky na základě příčinných kódů zamítnutí. Položky mohou být odstraněny (seznam může být vymazán) za specifických podmínek: 1) Po úspěšné registraci u sítě PLMN, která je v seznamu domovské sítě UE ([HPLMN](/mobilnisite/slovnik/hplmn/)) nebo její ekvivalentní domovské sítě ([EHPLMN](/mobilnisite/slovnik/ehplmn/)). 2) Manuálně uživatelem prostřednictvím menu výběru sítě v zařízení, což může spustit operaci 'vyhledání všech sítí'. 3) Potenciálně prostřednictvím aktualizací USIM přes vzdušné rozhraní ([OTA](/mobilnisite/slovnik/ota/)) od domovského operátora. Seznam má omezenou kapacitu (minimální je garantována specifikací), a pokud je plný, nejstarší položka může být nahrazena. Tento mechanismus hraje zásadní roli v efektivitě využití rádiových zdrojů, správě spotřeby energie zařízení a uživatelském komfortu tím, že odvádí UE od známých nedostupných sítí.

## K čemu slouží

Seznam FPLMN byl vytvořen k řešení problému neefektivních a vytrvalých pokusů o registraci, které vyčerpávají baterii UE a vytvářejí zbytečnou signalizační zátěž na rádiovém přístupu a v jádru sítě. V raných celulárních systémech bez takového seznamu by se UE, která byla sítí odmítnuta (např. z důvodu nedostatku roamingové smlouvy), mohla nepřetržitě znovu pokoušet o registraci pokaždé, když skenovala sítě nebo periodicky aktualizovala svou polohu, zejména v pohraničních oblastech nebo místech s překrývajícím se pokrytím od více operátorů.

Toto chování bylo plýtvavé a zhoršovalo uživatelský komfort. Koncept FPLMN zavedl do logiky výběru sítě v UE jakousi 'paměť'. Dočasným zablokováním odmítající sítě systém zajišťuje provozní efektivitu. Řeší tak omezení bezstavového výběrového procesu. Historický kontext zahrnuje jeho definici ve specifikacích GSM a jeho přenesení do procedur UMTS, LTE a 5G [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum). Seznam je obzvláště důležitý pro mezinárodní roaming, kde může UE narazit na mnoho sítí, z nichž pouze podmnožina má platné roamingové smlouvy s domovským operátorem. Umožňuje UE rychle se 'naučit' a vyhnout se sítím, které ji neobslouží, čímž zefektivňuje proces hledání povolené navštívené sítě. Podmínky pro vymazání seznamu, zejména po kontaktu s domovskou sítí, zajišťují, že UE nezůstane trvale zablokována pro síť, pokud je základní důvod zamítnutí (např. dočasné přerušení roamingové smlouvy) později vyřešen.

## Klíčové vlastnosti

- Trvale uložen na kartě USIM/SIM uvnitř UE
- Obsahuje identifikátory PLMN (MCC+MNC) sítí, které registraci odmítly
- Aktualizován automaticky UE na základě specifických příčinných kódů zamítnutí od sítě
- Zakazuje automatický výběr sítě/registraci na PLMN uvedené v seznamu
- Lze vymazat manuálně uživatelem iniciovaným skenováním sítí nebo automaticky po úspěšné registraci na HPLMN/EHPLMN
- Má definovanou minimální kapacitu úložiště (např. 4 položky) pro zvládnutí více zakázaných sítí

## Související pojmy

- [HPLMN – Home Public Land Mobile Network](/mobilnisite/slovnik/hplmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 22.811** (Rel-7) — Network Selection Mechanisms Overview
- **TS 31.121** (Rel-18) — UICC-terminal interface test specification

---

📖 **Anglický originál a plná specifikace:** [FPLMN na 3GPP Explorer](https://3gpp-explorer.com/glossary/fplmn/)
