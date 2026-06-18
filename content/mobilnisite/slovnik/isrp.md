---
slug: "isrp"
url: "/mobilnisite/slovnik/isrp/"
type: "slovnik"
title: "ISRP – Inter-System Routing Policies"
date: 2025-01-01
abbr: "ISRP"
fullName: "Inter-System Routing Policies"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/isrp/"
summary: "ISRP je soubor politik ANDSF (Access Network Discovery and Selection Function), který řídí uživatelské zařízení (UE) při směrování IP toků přes více dostupných přístupových sítí (např. 3GPP a non-3GPP"
---

ISRP je soubor politik ANDSF, který řídí uživatelské zařízení (UE) při směrování jeho IP toků přes více dostupných přístupových sítí a umožňuje inteligentní multi-přístupovou konektivitu na základě pravidel operátora.

## Popis

Politiky pro směrování mezi systémy (Inter-System Routing Policies – ISRP) jsou součástí architektury funkce pro vyhledávání a výběr přístupové sítě (Access Network Discovery and Selection Function – [ANDSF](/mobilnisite/slovnik/andsf/)) definované 3GPP. ANDSF je síťový prvek, který poskytuje uživatelskému zařízení (UE) politiky pro pomoc při vyhledávání a výběru dostupných přístupových sítí (jako LTE, [WLAN](/mobilnisite/slovnik/wlan/), WiMAX) a pro správu směrování provozu přes ně. ISRP konkrétně řídí rozhodnutí o směrování pro jednotlivé IP toky nebo skupiny toků (na základě faktorů jako cílová IP adresa, port nebo protokol). Umožňuje UE navázat a udržovat současná připojení k více přístupovým sítím (např. připojení [PDN](/mobilnisite/slovnik/pdn/) přes LTE a tunel [IPsec](/mobilnisite/slovnik/ipsec/) přes Wi-Fi) a směrovat provoz konkrétních aplikací přes nejvhodnější přístup podle pravidel politiky.

Architektura zahrnuje server ANDSF v síti operátora, který hostuje politiky ISRP, a klienta ANDSF v rámci UE. Komunikace probíhá přes rozhraní S14 (nebo přes [OMA](/mobilnisite/slovnik/oma/) [DM](/mobilnisite/slovnik/dm/)) pomocí protokolu OMA Device Management nebo [SOAP](/mobilnisite/slovnik/soap/)/[XML](/mobilnisite/slovnik/xml/). Politika ISRP se skládá z jednoho nebo více pravidel. Každé pravidlo obsahuje soubor výběrových kritérií (definujících, na které IP toky se vztahuje) a deskriptor směrování (určující preferovaný nebo zakázaný přístup pro tyto toky). Deskriptory směrování mohou specifikovat jediný přístup (např. "směrovat přes WLAN"), uspořádaný seznam přístupů nebo dokonce definovat scénář multi-přístupového připojení PDN (MAPCON) nebo mobility IP toků (IFOM). UE tato pravidla vyhodnocuje v definovaném pořadí priority, porovnává své aktivní IP toky s kritérii a určuje optimální směrovací cestu.

Fungování ISRP je řízeno politikami. Když se UE připojí k síti operátora podporující ANDSF, může vyžádat nebo přijmout politiky ISRP. IP vrstva a správce připojení v UE pak tyto politiky používají k rozhodování v reálném čase. Například pravidlo může určovat, že veškerý provoz pro streamování videa (identifikovaný konkrétním APN nebo rozsahem IP adres serveru) má být směrován přes připojení WLAN, pokud je dostupné a pokud je síla signálu WLAN nad prahovou hodnotou, jinak má dojít k návratu na 3GPP přístup. To umožňuje plynulé přesměrování provozu (offloading), vyrovnávání zátěže a výběr přístupu na základě služby. Úlohou ISRP je poskytnout operátorovi detailní kontrolu nad využitím síťových zdrojů a zlepšit uživatelský zážitek dynamickým výběrem nejlepšího dostupného přístupu pro každou službu, případně agregací šířky pásma nebo volbou nejnákladově efektivnější cesty.

## K čemu slouží

ISRP bylo vytvořeno pro řešení rostoucí složitosti heterogenních síťových prostředí, kde má UE současný přístup k více rádiovým technologiím (3GPP LTE/5G NR a non-3GPP jako Wi-Fi). Základním problémem byl nedostatek inteligentní, na politikách založené kontroly nad tím, jak je provoz z různých aplikací distribuován přes tyto dostupné cesty. Raná řešení byla binární (připojení buď k buněčné síti, nebo k Wi-Fi) nebo se spoléhala na jednoduché heuristiky na straně zařízení (jako síla signálu Wi-Fi), což často vedlo k neoptimálnímu výkonu, špatnému uživatelskému zážitku (např. "přilepená" Wi-Fi připojení) a neefektivnímu využití zdrojů operátora.

Zavedeno v 3GPP Release 10, ISRP bylo motivováno potřebou řízeného přesměrování provozu (traffic steering) a offloadingu ze strany operátora. Poskytlo operátorům nástroj pro implementaci obchodních pravidel (např. přesměrování provozu best-effort na Wi-Fi, udržení hlasu přes IMS na zabezpečené buněčné síti), optimalizaci síťového zatížení a umožnění pokročilých služeb jako plynulá mobilita toků. Odstranilo omezení předchozích neintegrovaných výběrových metod tím, že poskytlo standardizovaný, rozšiřitelný rámec politik, který mohl zohlednit širokou škálu dynamických podmínek (informace o objevených sítích, denní dobu, lokalitu, uživatelské preference) pro sofistikovaná rozhodnutí o směrování. Toto byl klíčový krok k naplnění vize Always Best Connected a později integrovaného 5G přístupu.

## Klíčové vlastnosti

- Směrování jednotlivých IP toků přes více přístupů na základě politik
- Integrace s architekturou ANDSF a referenčním bodem S14
- Podpora metod směrování: Multi-Access PDN Connectivity (MAPCON), IP Flow Mobility (IFOM) a non-seamless WLAN offload
- Systém založený na pravidlech s prioritizací, podmínkami platnosti a spouštěči aktualizace
- Umožňuje současnou multi-přístupovou konektivitu a inteligentní přesměrování provozu (traffic steering)
- Umožňuje kontrolu operátora s potenciálním zahrnutím uživatelských preferencí

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)
- [MAPCON – Multi Access PDN Connectivity](/mobilnisite/slovnik/mapcon/)
- [IFOM – IP Flow Mobility](/mobilnisite/slovnik/ifom/)

## Definující specifikace

- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification

---

📖 **Anglický originál a plná specifikace:** [ISRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/isrp/)
