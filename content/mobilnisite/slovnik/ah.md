---
slug: "ah"
url: "/mobilnisite/slovnik/ah/"
type: "slovnik"
title: "AH – Authentication Header"
date: 2025-01-01
abbr: "AH"
fullName: "Authentication Header"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/ah/"
summary: "AH je bezpečnostní protokol v rámci IPsec, který poskytuje bezstavovou integritu, autentizaci původu dat a volitelnou ochranu proti opětovnému přehrání pro IP pakety. Autentizuje celou hlavičku a dato"
---

AH je bezpečnostní protokol v rámci IPsec, který poskytuje bezstavovou integritu, autentizaci původu dat a volitelnou ochranu proti opětovnému přehrání pro IP pakety tím, že autentizuje celou hlavičku a datovou část.

## Popis

Authentication Header (AH) je základní součástí sady protokolů [IPsec](/mobilnisite/slovnik/ipsec/) (Internet Protocol Security), standardizované [IETF](/mobilnisite/slovnik/ietf/) a přijaté organizací 3GPP pro zabezpečení síťové komunikace. Funguje na síťové vrstvě (vrstva 3) a je definován v [RFC](/mobilnisite/slovnik/rfc/) 4302, přičemž 3GPP specifikuje jeho použití v rámci architektur systémů 3GPP v TS 33.210. AH poskytuje autentizační služby výpočtem kryptografického kontrolního součtu, známého jako Integrity Check Value (ICV), nad IP paketem. Tento ICV se vypočítává pomocí sdíleného tajného klíče a konkrétních autentizačních algoritmů, přičemž HMAC-SHA-1-96 a HMAC-MD5-96 byly běžně vyžadovány v raných vydáních 3GPP pro zajištění interoperability.

Z architektonického hlediska lze AH nasadit ve dvou režimech: transportním režimu a tunelovém režimu. V transportním režimu, typicky používaném pro zabezpečení typu end-to-end mezi hostiteli, je hlavička AH vložena za původní IP hlavičku a před protokol vyšší vrstvy (např. TCP, [UDP](/mobilnisite/slovnik/udp/)). Autentizuje datovou část IP paketu a neměnná pole IP hlavičky. V tunelovém režimu, používaném primárně pro zabezpečení mezi bránami (například mezi [PDN](/mobilnisite/slovnik/pdn/) Gateway uživatelského zařízení a firemním firewallem), je celý původní IP paket zapouzdřen do nového vnějšího IP paketu. Hlavička AH je vložena za tuto novou vnější IP hlavičku a autentizuje celý vnitřní IP paket spolu s neměnnými poli vnější IP hlavičky. To činí tunelový režim vhodným pro vytváření virtuálních privátních sítí ([VPN](/mobilnisite/slovnik/vpn/)).

Protokol funguje tak, že před IP datagram připojí hlavičku. Tato AH hlavička obsahuje několik polí: Next Header (identifikuje protokol následující datové části), Payload Length, Reserved, Security Parameters Index ([SPI](/mobilnisite/slovnik/spi/)), Sequence Number a Integrity Check Value (ICV). SPI v kombinaci s cílovou IP adresou a bezpečnostním protokolem (AH) jednoznačně identifikuje Security Association ([SA](/mobilnisite/slovnik/sa/)) pro daný paket. Sequence Number poskytuje ochranu proti opětovnému přehrání tím, že zajišťuje zpracování paketů pouze jednou. Příjemce použije stejný sdílený tajný klíč a algoritmus k přepočtu ICV a porovná jej s hodnotou v paketu. Pokud se shodují, je paket autentizován; pokud ne, je zahazen.

V rámci sítí 3GPP je role AH primárně definována pro zabezpečení rozhraní Za a Zb jako součásti frameworku Network Domain Security (NDS). Ochrana rozhraní Za se aplikuje mezi bezpečnostními doménami v rámci sítě 3GPP (např. mezi různými sítěmi operátorů nebo mezi operátorem a poskytovatelem služeb). Ochrana rozhraní Zb se aplikuje v rámci jedné bezpečnostní domény. Pro tato rozhraní 3GPP vyžaduje použití IPsec, přičemž AH je jedním ze dvou základních protokolů (spolu s ESP - Encapsulating Security Payload) dostupných k implementaci požadovaných bezpečnostních služeb. Jeho použití zajišťuje, že signalizační a uživatelský provoz mezi síťovými uzly, jako jsou MME, SGW a PGW, nemůže být pozměněn nebo falšován, což tvoří kritickou součást strategie obrany do hloubky jádrové sítě.

## K čemu slouží

AH byl vytvořen, aby řešil základní bezpečnostní slabiny původní sady protokolů IP, která neposkytovala žádné inherentní mechanismy pro autentizaci nebo integritu. IP pakety mohly být útočníky snadno padělány, modifikovány nebo znovu přehrávány, což činilo komunikaci přes nedůvěryhodné sítě, jako je internet, vnitřně rizikovou. IETF vyvinula IPsec, včetně AH, aby poskytla standardizované, interoperabilní zabezpečení na IP vrstvě. Tento přístup na vrstvě 3 je výhodný, protože dokáže transparentně zabezpečit všechny protokoly vyšších vrstev (TCP, UDP, ICMP atd.) bez nutnosti úprav jednotlivých aplikací.

V kontextu 3GPP bylo přijetí AH a IPsec motivováno evolucí směrem k plně IP jádrovým sítím. Jak se sítě 2G/3G vyvíjely na 4G LTE a 5G, jádrová síť (EPC, 5GC) se stala zcela založenou na IP. To přineslo nové hrozby, protože citlivá signalizace řídicí roviny a uživatelská data nyní procházela IP sítěmi, které mohly být sdílené nebo veřejné. Práce 3GPP na NDS/IP (TS 33.210) konkrétně směřovala ke standardizaci způsobu nasazení IPsec pro ochranu této komunikace mezi uzly. AH řeší problém zajištění, že zprávy přijaté mezi dvěma síťovými prvky 3GPP skutečně pocházejí z deklarovaného zdroje a nebyly během přenosu změněny, což je nezbytné pro účtování, legální odposlech a celkovou spolehlivost sítě.

Zatímco AH poskytuje silnou autentizaci a integritu, neposkytuje důvěrnost (šifrování). Toto omezení řeší jeho doplňkový protokol ESP. V mnoha praktických nasazeních 3GPP je ESP často preferován nebo používán spolu s AH, protože může poskytnout jak důvěrnost, tak autentizaci. AH však zůstává platnou a standardizovanou možností v rámci bezpečnostního frameworku 3GPP, zejména pro scénáře, kde je vyžadována autentizace a integrita, ale šifrování je buď nepotřebné, nebo řešeno jinými prostředky, nebo kde je autentizace původní IP hlavičky sama o sobě kriticky důležitá.

## Klíčové vlastnosti

- Poskytuje autentizaci původu dat pro IP pakety
- Zajišťuje bezstavovou integritu pro datovou část a hlavičku IP paketu
- Nabízí volitelnou ochranu proti opětovnému přehrání prostřednictvím sekvenčních čísel
- Funguje v transportním i tunelovém režimu
- Používá Security Associations (SA) identifikované trojicí SPI/cílová IP/protokol
- Spoléhá na sdílené tajné klíče a algoritmy jako HMAC-SHA-1 pro výpočet ICV

## Související pojmy

- [IPSec – Internet Protocol Security](/mobilnisite/slovnik/ipsec/)

## Definující specifikace

- **TS 33.210** (Rel-19) — UMTS Security for IP Networks

---

📖 **Anglický originál a plná specifikace:** [AH na 3GPP Explorer](https://3gpp-explorer.com/glossary/ah/)
