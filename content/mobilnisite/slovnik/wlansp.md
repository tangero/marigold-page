---
slug: "wlansp"
url: "/mobilnisite/slovnik/wlansp/"
type: "slovnik"
title: "WLANSP – WLAN Selection Policy"
date: 2026-01-01
abbr: "WLANSP"
fullName: "WLAN Selection Policy"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/wlansp/"
summary: "Soubor pravidel definovaných operátorem, poskytovaný uživatelskému zařízení (UE), který řídí jeho výběr a připojení k bezdrátovým lokálním sítím (WLAN). Automatizuje a optimalizuje rozhodnutí UE o pří"
---

WLANSP je soubor pravidel definovaných operátorem, který je poskytován uživatelskému zařízení (UE) za účelem automatizace a optimalizace výběru a připojení k bezdrátovým lokálním sítím (WLAN).

## Popis

[WLAN](/mobilnisite/slovnik/wlan/) Selection Policy (WLANSP) je klíčovou součástí objektu správy funkce [ANDSF](/mobilnisite/slovnik/andsf/) (Access Network Discovery and Selection Function). Jedná se o strukturovanou politiku založenou na [XML](/mobilnisite/slovnik/xml/), která poskytuje uživatelskému zařízení (UE) deterministická kritéria pro to, kdy a jak se připojit k dostupným WLAN sítím. Politika je dynamicky poskytována operátorovým serverem ANDSF uživatelskému zařízení přes referenční bod S14. Klient ANDSF v UE tyto pravidla interpretuje a vynucuje, čímž automatizuje proces výběru sítě, který by jinak byl manuální nebo založený na jednoduché síle signálu.

Politika obsahuje několik klíčových prvků. Zahrnuje informace pro objevování, které uvádějí dostupné přístupové sítě WLAN a jejich vlastnosti ([SSID](/mobilnisite/slovnik/ssid/), roamingoví partneři). Důležitější je, že obsahuje pravidla pro výběr. Jedná se o prioritizované příkazy typu "jestliže-pak", kde se podmínky (např. aktuální síla signálu buněčné sítě, kvalita WLAN signálu, denní doba, poloha, rychlost UE) vyhodnocují vůči prahovým hodnotám. Pokud jsou podmínky splněny, provede se akce pravidla, jako je připojení ke konkrétní WLAN, přesměrování konkrétních IP toků na WLAN nebo zákaz připojení. Politiky mohou být hierarchické, s globálními pravidly a konkrétnějšími výjimkami, a mohou být aktualizovány sítí na základě měnících se podmínek, jako je přetížení.

WLANSP funguje ve spolupráci s dalšími politikami ANDSF, jako jsou Inter-System Routing Policies ([ISRP](/mobilnisite/slovnik/isrp/)) a Inter-System Mobility Policies ([ISMP](/mobilnisite/slovnik/ismp/)). Zatímco ISRP/ISMP řídí směrování provozu mezi sítěmi 3GPP a WLAN pro aktivní připojení, WLANSP konkrétně spravuje počáteční výběr a připojení k samotnému přístupovému bodu WLAN. Její vynucování je kontinuální proces na pozadí; UE periodicky přehodnocuje podmínky politiky, aby zjistilo, zda se nestala dostupnou preferovanější WLAN, nebo zda by mělo být stávající připojení ukončeno. Tento mechanismus je klíčový pro implementaci strategií Wi-Fi offloadu řízených operátorem a pro zajištění vysoce kvalitního a bezproblémového uživatelského zážitku napříč heterogenními sítěmi.

## K čemu slouží

WLANSP byla vytvořena k řešení problému neefektivního a uživatelem řízeného výběru [WLAN](/mobilnisite/slovnik/wlan/), který často vedl ke špatnému výkonu sítě a nevyužití zdrojů Wi-Fi. Před [ANDSF](/mobilnisite/slovnik/andsf/) a WLANSP se uživatelská zařízení (UE) typicky připojovala k WLAN sítím pouze na základě uložených preferencí SSID a přijímané síly signálu, bez povědomí o zatížení jádrové sítě, kvalitě přenosové trasy WLAN nebo požadavcích uživatelských služeb. To vedlo k tomu, že se uživatelé připojovali k přetíženým nebo nekvalitním Wi-Fi sítím, i když byl dostupný silný signál buněčné sítě, což celkový zážitek zhoršovalo.

Motivací bylo dát mobilním operátorům inteligentní kontrolu nad chováním uživatelského zařízení při výběru přístupu v prostředí s více přístupy. Nasazením WLANSP mohli operátoři proaktivně spravovat distribuci provozu mezi své buněčné (3GPP) a Wi-Fi (non-3GPP) prostředky. Například operátor mohl definovat politiku pro přesměrování provozu snášejícího zpoždění na WLAN, když je buňka buněčné sítě přetížená, nebo pro připojení k Wi-Fi hotspotu provozovatelské kvality, když je UE stacionární a uvnitř budovy, aby poskytlo vyšší propustnost a šetřilo buněčné spektrum.

WLANSP, zavedená jako součást širšího rámce ANDSF ve verzi Release 8 a vylepšená v pozdějších verzích, představovala posun od vynucování politiky centrického k síti k vynucování centrickému k uživatelskému zařízení. Umožnila uživatelskému zařízení činit chytrá rozhodnutí v reálném čase na základě bohaté sady parametrů poskytovaných operátorem, což přesahovalo pouhé jednoduché přesměrování provozu a umožnilo skutečně optimalizované připojení s více přístupy. Toto byl základní koncept pro pozdější mechanismy směrování provozu a výběru sítě v 4G a 5G.

## Klíčové vlastnosti

- Struktura politiky založená na XML, poskytovaná přes rozhraní ANDSF S14
- Obsahuje prioritizované sady pravidel s podmíněnou logikou (if-then-else)
- Kritéria vyhodnocení zahrnují dostupnost RAT, sílu signálu, čas, polohu a rychlost UE
- Podporuje informace pro objevování WLAN sítí (SSID, HESSID atd.)
- Umožňuje automatický výběr WLAN a správu připojení řízenou operátorem
- Může být dynamicky aktualizována sítí na základě měnících se podmínek

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [ISRP – Inter-System Routing Policies](/mobilnisite/slovnik/isrp/)
- [ISMP – Inter-System Mobility Policy](/mobilnisite/slovnik/ismp/)

## Definující specifikace

- **TS 23.503** (Rel-20) — 5G Policy and Charging Control Framework
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 24.526** (Rel-19) — UE Policies for 5GS; Stage 3

---

📖 **Anglický originál a plná specifikace:** [WLANSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/wlansp/)
