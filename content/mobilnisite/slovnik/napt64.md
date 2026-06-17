---
slug: "napt64"
url: "/mobilnisite/slovnik/napt64/"
type: "slovnik"
title: "NAPT64 – Network Address and Port Translation IPv6 to IPv4"
date: 2025-01-01
abbr: "NAPT64"
fullName: "Network Address and Port Translation IPv6 to IPv4"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/napt64/"
summary: "NAPT64 je přechodový mechanismus umožňující klientům pouze s IPv6 komunikovat se servery pouze s IPv4 překladem IPv6 adres a portů na IPv4. Je nezbytný pro migraci na IPv6, neboť umožňuje operátorům z"
---

NAPT64 je přechodový mechanismus, který umožňuje klientům pouze s IPv6 komunikovat se servery pouze s IPv4 překladem IPv6 adres a portů na IPv4, čímž podporuje migraci na IPv6 při zachování zpětné kompatibility.

## Popis

NAPT64 funguje jako stavová funkce překladu síťových adres a portů (Network Address and Port Translation), která se typicky nasazuje na hranici mezi přístupovou sítí pouze s IPv6 a internetem IPv4. Její architektura zahrnuje překladač, který zachytává pakety od hostitelů IPv6 určené pro servery IPv4. Překladač udržuje vazební tabulku, která mapuje zdrojovou IPv6 adresu a port na syntetizovanou IPv4 adresu a port z fondu dostupných IPv4 adres. Když hostitel IPv6 zahájí relaci s cílem IPv4, zařízení NAPT64 vytvoří záznam mapování. Přepíše hlavičku paketu IPv6, převede zdrojovou adresu/port IPv6 na adresu/port IPv4 ze svého fondu a cílovou IPv4 adresu na syntetizovanou IPv6 adresu (často s použitím předdefinované IPv6 předpony, jako je 64:ff9b::/96, pro známé IPv4 adresy). Návratový provoz ze serveru IPv4 je zpětně přeložen pomocí vazební tabulky, což zajišťuje, že hostitel IPv6 obdrží odpověď. Mezi klíčové komponenty patří funkce překladače, fond IPv4 adres a stavová tabulka vazeb pro správu relací. Jeho role je klíčová v architekturách dual-stack lite (DS-Lite) a dalších přechodových architekturách IPv6, kde funguje jako operátorský [NAT](/mobilnisite/slovnik/nat/) (CGN) pro provoz z IPv6 na IPv4, čímž šetří omezené IPv4 adresy a usnadňuje plynulejší přechod na sítě IPv6.

## K čemu slouží

NAPT64 byl vytvořen, aby řešil vyčerpání IPv4 adres a postupnou migraci na sítě IPv6. Když operátoři začali nasazovat přístupové sítě pouze s IPv6, objevil se významný problém: jak umožnit těmto klientům pouze s IPv6 přístup k naprosté většině internetových služeb, které jsou stále hostovány na IPv4. Tradiční duální zásobník (podpora IPv4 i IPv6 na každém zařízení) nebyl vždy proveditelný kvůli nedostatku IPv4 adres. NAPT64 to řeší tím, že umožňuje zařízením pouze s IPv6 komunikovat se servery IPv4 bez nutnosti plného IPv4 zásobníku na klientovi, čímž zjednodušuje síťovou architekturu a snižuje provozní náklady. Je klíčovou součástí strategií přechodu na IPv6, neboť umožňuje postupnou likvidaci infrastruktury IPv4 při zachování kontinuity služeb.

## Klíčové vlastnosti

- Stavový překlad IPv6 adres/portů na IPv4 adresy/porty
- Podpora přístupu klientů pouze s IPv6 k serverům pouze s IPv4
- Využití fondu IPv4 adres pro překladová mapování
- Správa vazební tabulky pro stav relace
- Kompatibilita s DNS64 pro bezproblémové překlad jmen
- Umožňuje funkci operátorského NAT (CGN) v sítích IPv6

## Související pojmy

- [NAT64 – Network Address Translation IPv6 to IPv4](/mobilnisite/slovnik/nat64/)

## Definující specifikace

- **TR 23.975** (Rel-19) — IPv6 Transition Scenarios for 3GPP Networks

---

📖 **Anglický originál a plná specifikace:** [NAPT64 na 3GPP Explorer](https://3gpp-explorer.com/glossary/napt64/)
