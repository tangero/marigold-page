---
slug: "suci"
url: "/mobilnisite/slovnik/suci/"
type: "slovnik"
title: "SUCI – Subscription Concealed Identifier"
date: 2026-01-01
abbr: "SUCI"
fullName: "Subscription Concealed Identifier"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/suci/"
summary: "SUCI je ochranný identifikátor používaný uživatelským zařízením (UE) během počáteční registrace do sítě před autentizací. Jedná se o kryptografickou konstrukci, která skrývá trvalý identifikátor předp"
---

SUCI je ochranný, šifrovaný identifikátor používaný mobilním zařízením při počátečním přístupu do sítě, který skrývá uživatelův trvalý identifikátor předplatného a brání sledování přes rozhraní vzdušného rozhraní.

## Popis

Subscription Concealed Identifier (SUCI) je základní bezpečnostní a soukromí chránicí funkce zavedená v 5G, definovaná ve specifikaci 3GPP Release 15. Jedná se o jednorázově použitý identifikátor vysílaný uživatelským zařízením (UE) namísto trvalého Subscription Permanent Identifier ([SUPI](/mobilnisite/slovnik/supi/)) během počáteční registrační procedury, konkrétně v Registration Request zprávě. SUCI je generováno samotným UE pomocí standardizovaného schématu nazvaného [ECIES](/mobilnisite/slovnik/ecies/) (Elliptic Curve Integrated Encryption Scheme) profil A. UE zašifruje SUPI pomocí veřejného klíče funkce Subscription Identifier De-concealing Function ([SIDF](/mobilnisite/slovnik/sidf/)) domovské sítě, který je bezpečně uložen v UE (např. v Universal Integrated Circuit Card (UICC)). Výstupem je řetězec obsahující identifikátor veřejného klíče domovské sítě, identifikátor schématu ECIES, šifrový text a [MAC](/mobilnisite/slovnik/mac/) tag.

Po přijetí SUCI jej servisní síť (např. navštívená veřejná pozemní mobilní síť ([VPLMN](/mobilnisite/slovnik/vplmn/))) přepošle jako součást autentizační procedury do domovské sítě ([HPLMN](/mobilnisite/slovnik/hplmn/)). Funkce SIDF domovské sítě, která drží odpovídající privátní klíč, je jedinou entitou schopnou dešifrovat SUCI a získat čistý text SUPI. Toto dešifrování probíhá uvnitř funkce Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) nebo Authentication Server Function ([AUSF](/mobilnisite/slovnik/ausf/)) domovské sítě. SUPI je pak použito pro autentizaci účastníka a odvození 5G Globally Unique Temporary Identifier (5G-GUTI) pro následující signalizaci. Zásadní je, že servisní síť nikdy nevidí SUPI v čitelné podobě, čímž je chráněna trvalá identita účastníka před navštíveným operátorem a jakýmikoli pasivními odposlouchávači na rádiovém spoji.

Architektura pro SUCI zahrnuje několik síťových funkcí. UE obsahuje aplikaci USIM, která uchovává veřejný klíč domovské sítě a provádí šifrování. Access and Mobility Management Function (AMF) v servisní síti přijímá SUCI a směruje jej do příslušné domovské sítě. SIDF, typicky umístěná společně s UDM/AUSF, provádí odtajnění. Použití SUCI je povinné pro počáteční registraci v 5G, pokud UE nemá platné 5G-GUTI, což z něj činí základní kámen zvýšeného soukromí účastníka v 5G. Jeho použití se řídi nastavením soukromí účastníka, ale výchozím a doporučeným režimem je vždy použít SUCI pro počáteční registraci, což představuje významný posun oproti 4G, kde byl trvalý International Mobile Subscriber Identity (IMSI) často odesílán v čitelné podobě během počátečního připojení.

## K čemu slouží

SUCI bylo vytvořeno, aby vyřešilo kritickou a dlouhodobou zranitelnost soukromí v mobilních sítích: vystavení trvalé identity účastníka (IMSI v 2G/3G/4G) přes rádiové rozhraní. V předchozích generacích byl IMSI často přenášen v čitelné podobě během počátečního připojení k síti nebo v určitých scénářích selhání. To umožňovalo pasivním odposlouchávačům s levným vybavením (IMSI catchery nebo stingrays) sledovat polohy a pohyby jednotlivců, provádět cílené útoky nebo mapovat identity. Tato zranitelnost byla hlavním problémem soukromí a narušovala důvěru uživatelů.

Motivace pro SUCI vycházela z regulatorních tlaků (např. GDPR), zvýšeného společenského povědomí o digitálním soukromí a technické příležitosti, kterou poskytl nový návrh 5G core sítě (5GC). 3GPP navrhlo SUCI jako klíčovou součást architektury zvýšeného soukromí účastníka v 5G. Řeší omezení předchozích dočasných identifikátorů (jako TMSI/GUTI), které nemohly být vždy použity – pokud UE vstoupilo do nové oblasti bez platného dočasného ID, muselo přejít na odeslání IMSI v čitelné podobě. SUCI tuto záložní zranitelnost odstraňuje tím, že zajišťuje, že trvalá identita není nikdy vystavena, ani při prvním kontaktu.

Navíc SUCI podporuje oddělení servisní sítě od domovské sítě z hlediska znalosti identity. To odpovídá principům síťového řezání a architektury založené na službách v 5G, kde by servisní síť měla poskytovat konektivitu bez nutnosti znát skutečnou identitu účastníka. Řešením problému všudypřítomného sledování umožňuje SUCI bezpečnější a soukromí respektující případy použití, včetně kritických IoT a vládních služeb, kde je anonymita zařízení prvořadá až do autentizace doménou domovské sítě.

## Klíčové vlastnosti

- Kryptografické skrytí SUPI pomocí šifrování veřejným klíčem (ECIES)
- Generováno UE pomocí veřejného klíče domovské sítě
- Dešifrováno pouze funkcí SIDF domovské sítě pomocí privátního klíče
- Zabraňuje pasivnímu odposlechu a útokům pomocí IMSI catcherů
- Odstraňuje přenos trvalé identity účastníka v čitelné podobě
- Nedílná součást procedury primární autentizace a dohody o klíči v 5G (5G-AKA)

## Související pojmy

- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)
- [5G-GUTI – 5G Globally Unique Temporary Identifier](/mobilnisite/slovnik/5g-guti/)
- [AUSF – Authentication Server Function](/mobilnisite/slovnik/ausf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TS 23.003** (Rel-19) — Numbering, addressing and identification in 3GPP
- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 31.122** (Rel-18) — USIM Conformance Test Specification
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures
- **TS 33.514** (Rel-20) — 5G Security Assurance for UDM
- **TS 33.835** (Rel-16) — Study on authentication and key management for apps
- **TR 33.841** (Rel-16) — Security aspects; Study on 256-bit algorithms for 5G

---

📖 **Anglický originál a plná specifikace:** [SUCI na 3GPP Explorer](https://3gpp-explorer.com/glossary/suci/)
